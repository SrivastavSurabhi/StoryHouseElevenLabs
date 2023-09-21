from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from .models import *
from django_datatables_view.base_datatable_view import BaseDatatableView
import os
from pdfminer.high_level import extract_text
import requests
import openai
from django.views.static import serve
import ebooklib
from ebooklib import epub
import pdfkit
import mobi
import html2text
import re
import json
from moviepy.editor import concatenate_audioclips, AudioFileClip
from bs4 import BeautifulSoup
from functools import partial

media_path = settings.MEDIA_ROOT
pdfPath = media_path + 'home/esmee/mouthpiece/pdfs/'
textPath = media_path + 'home/esmee/mouthpiece/text/'
mp3Path = media_path + 'home/esmee/mouthpiece/mp3s/'
ebookPath = media_path + 'home/esmee/mouthpiece/ebooks/'
summaryPath = media_path + 'home/esmee/mouthpiece/summaries/'
htmlPath = media_path + 'home/esmee/mouthpiece/htmls/'
openai.api_key = os.environ.get('OPENAI_API_KEY')


def media_files(request, path):
    try:
        if request.user.is_authenticated:
            if 'ebook' in path.split('/')[3]:
                if 'epub' in path:
                    return serve(request, path.replace('.epub', '.pdf'), document_root=settings.MEDIA_ROOT)
                else:
                    return serve(request, path.replace('.mobi', '.pdf'), document_root=settings.MEDIA_ROOT)
            return serve(request, path, document_root=settings.MEDIA_ROOT)
        else:
            if 'pdf' in path.split('/')[3]:
                file = PDF.objects.filter(name=path.split('/')[4])[0]
            elif 'html' in path.split('/')[3]:
                file = HTML.objects.filter(name=path.split('/')[4])[0]
            elif 'ebook' in path.split('/')[3]:
                file = EPUB.objects.filter(name=path.split('/')[4])[0]
                if file.is_public:
                    if 'epub' in path:
                        return serve(request, path.replace('.epub', '.pdf'), document_root=settings.MEDIA_ROOT)
                    else:
                        return serve(request, path.replace('.mobi', '.pdf'), document_root=settings.MEDIA_ROOT)
            if file.is_public:
                return serve(request, path, document_root=settings.MEDIA_ROOT)
            return redirect('dashboard')
    except:
        return serve(request, path, document_root=settings.MEDIA_ROOT)


def html(request):
    return render(request, 'html-files.html')


def mp3(request):
    return render(request, 'mp3-files.html')


def summary(request):
    return render(request, 'summaries.html')


def public(request):
    return render(request, 'public.html')

def textfiles(request):
    return render(request, 'textfile.html')


def savepdf(request):
    if request.method == 'POST':
        newdoc = request.FILES.getlist('files')
        try:
            alreadyexist = []
            for doc in newdoc:
                file = os.path.splitext(doc.name)
                if file[1] == '.pdf':
                    try:
                        PDF.objects.get(name=doc.name, user=request.user)
                        alreadyexist.append(doc.name)
                    except:
                        PDF.objects.create(name=doc.name, path=pdfPath + doc.name, user=request.user)
                        with open(pdfPath + doc.name, 'wb+') as f:
                            for chunk in doc.chunks():
                                f.write(chunk)
                else:
                    try:
                        EPUB.objects.get(name=doc.name, user=request.user)
                        alreadyexist.append(doc.name)
                    except:
                        EPUB.objects.create(name=doc.name, path=pdfPath + doc.name, user=request.user)
                        with open(ebookPath + doc.name, 'wb+') as f:
                            for chunk in doc.chunks():
                                f.write(chunk)
                        try:
                            epub_to_pdf(ebookPath + doc.name, ebookPath + file[0] + '.pdf')
                        except:
                            pass
            if len(alreadyexist) > 0:
                return JsonResponse({'status': 'error', 'message': 'Files ' if len(alreadyexist) > 1 else 'File '+ ', '.join(alreadyexist)+' already exist.', 'tag': 'error'})
            else:
                return JsonResponse({'status': 'success', 'message': 'Files Uploaded', 'tag': 'success'})
        except:
            return JsonResponse({'status': 'error', 'message': 'Files not Uploaded', 'tag': 'error'})
    # return redirect('home')

def savetext(request):
    if request.method == 'POST':
        newdoc = request.FILES.getlist('files')
        try:
            alreadyexist = []
            for doc in newdoc:
                file = os.path.splitext(doc.name)
                if file[1] == '.txt':
                    try:
                        Text.objects.get(name=doc.name, user=request.user)
                        alreadyexist.append(doc.name)
                    except:
                        Text.objects.create(name=doc.name, path=textPath + doc.name, user=request.user)
                        with open(textPath + doc.name, 'wb+') as f:
                            for chunk in doc.chunks():
                                f.write(chunk)
                else:
                    return JsonResponse({'status': 'error', 'message': 'Files not Uploaded', 'tag': 'error'})
            if len(alreadyexist) > 0:
                return JsonResponse({'status': 'error', 'message': 'Files ' if len(alreadyexist) > 1 else 'File '+ ', '.join(alreadyexist)+' already exist.', 'tag': 'error'})
            else:
                return JsonResponse({'status': 'success', 'message': 'Files Uploaded', 'tag': 'success'})
        except:
            return JsonResponse({'status': 'error', 'message': 'Files not Uploaded', 'tag': 'error'})

def pdftohtmlandtext(request):
    if request.method == 'POST':
        file_name = request.POST['file_name'].split(',')
        for file in file_name:
            try:
                docs = os.path.splitext(file)
                if docs[1] == '.pdf':
                    htmlText = extract_text(pdfPath + file)
                    text = extract_text(pdfPath + file)
                    htmlFile = file.replace('.pdf', '.html')
                    textFile = file.replace('.pdf', '.txt')
                    pdfobj = PDF.objects.get(name=file, user=request.user)

                elif docs[1] == '.mobi':
                    tempdir, filepath = mobi.extract(ebookPath + file)
                    file_text = open(filepath, encoding="utf8")
                    htmlText = file_text.read()
                    text = html2text.html2text(htmlText)
                    # text = mobi.extract(ebookPath + file)
                    htmlFile = file.replace('.mobi', '.html')
                    textFile = file.replace('.mobi', '.txt')
                    pdfobj = EPUB.objects.get(name=file, user=request.user)

                else:
                    htmlText = epub_to_html(ebookPath + file)
                    text = epub_to_text(ebookPath + file)
                    htmlFile = file.replace('.epub', '.html')
                    textFile = file.replace('.epub', '.txt')
                    pdfobj = EPUB.objects.get(name=file, user=request.user)

                doc = open(htmlPath + htmlFile, "w", encoding="utf-8")
                doc.write("<html>\n<head>\n</head> <body><p>"+re.sub(r'\s{2,}', ' ', remove_unknown_characters(htmlText, docs[1],'html'))+"</p> \n</body></html>")

                text_doc = open(textPath + textFile, "w", encoding="utf-8")
                if docs[1] == '.mobi':
                    text = remove_unknown_characters(text, docs[1],'text')
                text_doc.write(text)
                
                # Saving the data into the HTML file              
                HTML.objects.create(name=htmlFile, path=htmlFile, user=request.user, text=text, parent_file='{"name": "'+pdfobj.name+'", "id": "'+str(pdfobj.id)+'", "type": "'+docs[1]+'"}')
                Text.objects.create(name=textFile, path=textFile, user=request.user, text=text, total_charachter=len(text),parent_file='{"name": "'+pdfobj.name+'", "id": "'+str(pdfobj.id)+'", "type": "'+docs[1]+'"}')
                pdfobj.status = True
                pdfobj.save()
                doc.close()
                text_doc.close()
            except:
                return JsonResponse({'Success': False, "message": "HTML not created Please try again or try with other file.", "status": "error"})
    return JsonResponse({'Success': True, "message": "HTML & Text created.", "status": "success"})


def rename_text_files_path(request):
    texts = Text.objects.filter()
    for text in texts:
        text.path = text.name
        text.save()
    return JsonResponse({"Success":"true"})


def get_length_of_txt_file(request):
    file_path = request.GET['file_path']
    print(file_path)
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
    return JsonResponse({'Success': True, "message": "HTML & Text created.", "status": "success","length":len(content)})

def split_file_into_chunks(file_path, chunk_size):
    with open(file_path, 'r') as file:
        content = file.read()
    sentences = re.split(r'(?<=[.!?])\s+', content)
    chunks = []
    current_chunk = ''
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += sentence
        else:
            chunks.append(current_chunk)
            current_chunk = sentence
    chunks.append(current_chunk)
    for i, chunk in enumerate(chunks):
        with open(f'output_chunk_{i+1}.txt', 'w') as file:
            file.write(chunk)


def divide_chunks(request):
    file_path = request.GET['file_path']
    file_name = file_path.split('/')[-1]
    text_obj = Text.objects.filter(name=file_name)
    chunks_size = int(request.GET['chunks_size'])
    with open(file_path, 'r') as file:
        content = file.read()
    sentences = re.split(r'(?<=[.!?])\s+', content)
    if len(sentences) == 1 and len(sentences[0])>500:
        sentences = re.findall(r'[^.!?]*[.!?](?!\s|$)', content, flags=re.MULTILINE)
    chunks = []
    # created_files = []
    current_chunk = ''
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunks_size:
            current_chunk += sentence
        else:
            chunks.append(current_chunk)
            current_chunk = sentence
    chunks.append(current_chunk)
    for i, chunk in enumerate(chunks):
        file_n = file_path.split('/text/')[0]+'/text/'+file_name.split('.txt')[0]+str(i+1)
        with open(file_n+'.txt', 'w') as file:
            file.write(chunk)
            file.close()
            # created_files.append(file_n+'.txt')
            Text.objects.create(name=file_n.split('/')[-1]+'.txt', path=file_n.split('/')[-1]+'.txt', user=request.user, text=chunk, total_charachter=len(chunk),parent_file='{"name": "'+file_name+'", "id": "'+str(text_obj.last().id)+'", "type": ".txt"}')
    return JsonResponse({'Success': True, "message": "Text Files created.", "status": "success"})


def split_text_to_words(text, max_length=5000):
    words = []
    current_word = ''

    for word in text.split():
        if len(current_word) + len(word) + 1 <= max_length:
            current_word += ' ' + word
        else:
            words.append(current_word.strip())
            current_word = word

    if current_word:
        words.append(current_word.strip())

    return words


def get_file_names(folder_path):
    file_names = []
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            file_names.append(file_name)
    return file_names


def convert_to_mp3(request):
    data = request.POST
    file_name = data['file_name']
    voice_id = data['voice_id']
    stability = data['stability']
    similarity = data['similarity']
    doc = os.path.splitext(file_name)[0]
    try:
        html = HTML.objects.filter(user=request.user, name=file_name)[0]
        words = split_text_to_words(html.text)
        count = 0
        directory = doc
        current_time = str(datetime.now()).replace(' ','-').replace(':','-').split('.')[0]
        path = os.path.join(mp3Path, directory+current_time)
        if not os.path.exists(path):
            os.mkdir(path)
        path_name = path
        for word in words:
            count = count+1

            CHUNK_SIZE = 1024
            url = "https://api.elevenlabs.io/v1/text-to-speech/"+voice_id #EXAVITQu4vr4xnSDxMaL""
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": os.environ.get('ELEVENLABS_API_KEY')
            }

            data = {
                "text": word,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": stability,
                    "similarity_boost": similarity
                }
            }

            response = requests.post(url, json=data, headers=headers)

            if response.status_code == 200:
                with open(path_name+'/'+doc+str(count)+'.mp3', 'wb') as f:
                    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                        if chunk:
                            f.write(chunk)
            else:
                return JsonResponse({'status': response.status_code, 'message': response.text})

        audioList = []
        file_dir = get_file_names(path_name)
        sorted_filenames = sorted(file_dir, key=partial(get_numeric_part, prefix=doc))
        for num in sorted_filenames:
            audioList.append(AudioFileClip(path_name+'/'+num))

        final_audio = concatenate_audioclips(audioList)
        final_audio.write_audiofile(path_name+"/"+doc+".mp3")

        MP3.objects.create(name=path_name.split('/')[-1]+'/'+doc+'.mp3', path=path_name+"/"+doc+".mp3", user=request.user)
        html.text_to_speech_status = True
        html.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': e})


def get_numeric_part(filename, prefix):
    return int(filename.split(prefix)[1].split('.mp3')[0])


def move_to_public(request):
    file_name = request.POST['file_name']
    doc = os.path.splitext(file_name)[1]
    if doc == ".pdf":
        file = PDF.objects.get(user=request.user, name=file_name)
    if doc == ".html":
        file = HTML.objects.get(user=request.user, name=file_name)
    if doc == ".epub" or doc == ".mobi":
        file = EPUB.objects.get(user=request.user, name=file_name)
    file.is_public = True
    file.save()
    return JsonResponse({'status': 'success'})


def epub_to_pdf(input_file, output_file):
    try:
        book = epub.read_epub(input_file)
        content = ""
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                content += item.get_content().decode('utf-8')  # Decode bytes to string
    except:
        tempdir, filepath = mobi.extract(input_file)
        file_text = open(filepath, encoding="utf8")
        content = file_text.read()
        text = html2text.html2text(content)
        content = text

    html_content = f"<html><body>{content}</body></html>"
    config = pdfkit.configuration(wkhtmltopdf=os.getenv("WKHTML_TO_PDF_PATH"))
    pdfkit.from_string(html_content, output_file, configuration=config)


def home(request):
    return redirect('dashboard')


class pdfListView(BaseDatatableView):
    columns = ['id', 'name', 'path', 'status', 'upload_on', 'is_public']

    def get_initial_queryset(self):
        return PDF.objects.filter(user=self.request.user).order_by('status')


class epubListView(BaseDatatableView):
    columns = ['id', 'name', 'path', 'status', 'upload_on', 'is_public']

    def get_initial_queryset(self):
        return EPUB.objects.filter(user=self.request.user).order_by('status')


class htmlListView(BaseDatatableView):
    columns = ['id', 'name', 'path', 'text_to_speech_status', 'upload_on', 'summary_status', 'is_public']

    def get_initial_queryset(self):
        return HTML.objects.filter(user=self.request.user).order_by('text_to_speech_status')


class mp3ListView(BaseDatatableView):
    columns = ['id', 'name', 'path', 'status', 'upload_on']

    def get_initial_queryset(self):
        return MP3.objects.filter(user=self.request.user).order_by('status')


class summaryListView(BaseDatatableView):
    columns = ['name', 'upload_on']

    def get_initial_queryset(self):
        return Summary.objects.filter(user=self.request.user)


class publicFileListView(BaseDatatableView):
    columns = ['name', 'upload_on']

    def get_initial_queryset(self):
        html = HTML.objects.filter(user=self.request.user, is_public=True).values_list("name", "upload_on", "id")
        pdf = PDF.objects.filter(user=self.request.user, is_public=True).values_list("name", "upload_on", "id")
        epub = EPUB.objects.filter(user=self.request.user, is_public=True).values_list("name", "upload_on", "id")
        return (pdf.union(epub)).union(html)

    def filter_queryset(self, qs):
        return qs

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            json_data.append([
                {"name": item[0]},
                {"upload_on": item[1]},
                {"id": item[2]},
            ])
        return json_data
    

class textFileListView(BaseDatatableView):
    columns = ['id','name','upload_on']

    def get_initial_queryset(self):
        html = Text.objects.filter(user=self.request.user).values("id","name", "upload_on","path","total_charachter")
        return html

    def filter_queryset(self, qs):
        return qs

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            print(item)
            json_data.append({
                "id": item['id'],
                "name": item['name'],
                "upload_on": item['upload_on'].date(),
                "path":item['path'].split('\\')[-1],
                "total_charachter":item['total_charachter']
            })
        return json_data


def remove_unknown_characters(text, file,type):
    pattern = r'[^\x00-\x7F]+'
    cleaned_text = re.sub(pattern, '', text)
    if file == '.pdf' or file == '.mobi':
        cleaned_text = re.sub(r'\n{3,}', '\n', cleaned_text)
        if type == 'html':
            cleaned_text = cleaned_text.replace('\n', '<br>')
    return cleaned_text


def createsummmary(request):
    if request.method == 'POST':
        file_name = request.POST['file_name'].split(',')
        notProcessed = []
        largefiles = []
        for file in file_name:
            try:
                html = HTML.objects.get(name=file, user=request.user)
                text = html.text
                file_name = os.path.splitext(file)
                if len(text.split()) > 3000:
                    largefiles.append(file)
                    notProcessed.append(file)
                else:
                    doc = open(summaryPath + file_name[0] + '.txt', "w", encoding="utf-8")
                    doc.write(text)
                    doc.close()
                    openairesponse = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "user", "content": "Summarize: "+text},
                        ]
                    )
                    summaryText = openairesponse.choices[0].message.content
                    Summary.objects.create(name=file_name[0]+'.txt', path=file_name[0]+'.txt', user=request.user, text=summaryText)
                    html.summary_status = True
                    html.save()
            except:
                notProcessed.append(file)
        if len(notProcessed) > 0:
            return JsonResponse({'status': 'error', 'message': 'file '+', '.join(notProcessed) + ' summary not created.', 'largefiles': True if len(largefiles) else False})
        if len(largefiles) > 0:
            return JsonResponse({'status': 'error', 'largefiles': True})
    return JsonResponse({'status': 'success', 'message': 'Summary created.'})


def epub_to_html(epub_file):
    book = epub.read_epub(epub_file)
    text = ""
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            html = item.get_content()
            text += html.decode('utf-8')
    return text

def epub_to_text(epub_file_path):
    text=""
    book = epub.read_epub(epub_file_path)
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            for script in soup(["script", "style"]):
                script.extract()
            text += soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


def delete_pdf(request, id):
    try:
        PDF.objects.get(user=request.user, id=id).delete()
        return JsonResponse({'status': 'success', 'message': 'File deleted.'})
    except:
        return JsonResponse({'status': 'error', 'message': 'File not deleted.'})
    
def delete_text(request, id):
    try:
        Text.objects.get(user=request.user, id=id).delete()
        return JsonResponse({'status': 'success', 'message': 'File deleted.'})
    except:
        return JsonResponse({'status': 'error', 'message': 'File not deleted.'})


def delete_epub(request, id):
    try:
        EPUB.objects.get(user=request.user, id=id).delete()
        return JsonResponse({'status': 'success', 'message': 'File deleted.'})
    except:
        return JsonResponse({'status': 'error', 'message': 'File not deleted.'})


def delete_html_file(request, id):
    try:
        html = HTML.objects.get(user=request.user, id=id)
        val = json.loads(html.parent_file)
        try:
            if val['type'] == ".pdf":
                fileobj = PDF.objects.get(id=val['id'])
            else:
                fileobj = EPUB.objects.get(id=val['id'])
            fileobj.status = False
            fileobj.save()
        except:pass
        html.delete()
        return JsonResponse({'status': 'success', 'message': 'File deleted.'})
    except:
        return JsonResponse({'status': 'error', 'message': 'File not deleted.'})


def delete_mp3_file(request, id):
    try:
        mp3 = MP3.objects.get(user=request.user, id=id)
        try:
            fileobj = HTML.objects.get(user=request.user, name=(os.path.splitext(mp3.name)[0]+'.html').split('/')[1])
            fileobj.text_to_speech_status = False
            fileobj.save()
        except:pass
        mp3.delete()
        return JsonResponse({'status': 'success', 'message': 'File deleted.'})
    except:
        return JsonResponse({'status': 'error', 'message': 'File not deleted.'})


def delete_summary_file(request, id):
    try:
        summary = Summary.objects.get(user=request.user, id=id)
        try:
            fileobj = HTML.objects.get(user=request.user, name=os.path.splitext(summary.name)[0]+'.html')
            fileobj.summary_status = False
            fileobj.save()
        except:pass
        summary.delete()
        return JsonResponse({'status': 'success', 'message': 'File deleted.'})
    except:
        return JsonResponse({'status': 'error', 'message': 'File not deleted.'})


def delete_public_file(request, id):
    try:
        name = request.GET['name']
        docs = os.path.splitext(name)[1]
        if docs == '.pdf':
            fileobj = PDF.objects.get(id=id)
        elif docs == '.html':
            fileobj = HTML.objects.get(id=id)
        else:
            fileobj = EPUB.objects.get(id=id)
        fileobj.is_public = False
        fileobj.save()
        return JsonResponse({'status': 'success', 'message': 'File deleted.'})
    except:
        return JsonResponse({'status': 'error', 'message': 'File not deleted.'})
