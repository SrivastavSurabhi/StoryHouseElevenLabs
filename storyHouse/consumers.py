from django.conf import settings
from django.http import JsonResponse
from textToSpeech.models import *
import os
import requests
from moviepy.editor import concatenate_audioclips, AudioFileClip
from functools import partial
import json
from channels.generic.websocket import WebsocketConsumer


media_path = settings.MEDIA_ROOT
mp3Path = media_path + 'home/esmee/mouthpiece/mp3s/'

  
class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
  
    def disconnect(self, close_code):
        self.close()   
  
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.send(text_data=json.dumps({'status': 'processed'}))
        data = text_data_json['data']
        file_name = data['file_name']
        voice_id = data['voice_id']
        stability = data['stability']
        similarity = data['similarity']
        username = data['username']
        doc = os.path.splitext(file_name)[0]
        try:
            html = HTML.objects.filter(user=username, name=file_name)[0]
            words = split_text_to_words(html.text)
            count = 0
            directory = doc
            current_time = str(datetime.now()).replace(' ','-').replace(':','-').split('.')[0]
            path = os.path.join(mp3Path, directory+current_time)
            if not os.path.exists(path):
                os.mkdir(path)
            path_name = path
            self.send(text_data=json.dumps({'status': 'Processing mp3(Divided html file into '+str(len(words)) +' chunks)'}))
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
                    self.send(text_data=json.dumps({'status':'MP3 generated of chunk '+ str(count) +'/'+ str(len(words))}))
                else:
                    self.send(text_data=json.dumps({'status':response.text}))
                    self.close()
                    # return JsonResponse({'status': response.status_code, 'message': response.text})

            self.send(text_data=json.dumps({'status': 'Conversion to speech is completed.'}))
            audioList = []
            file_dir = get_file_names(path_name)
            sorted_filenames = sorted(file_dir, key=partial(get_numeric_part, prefix=doc))
            for num in sorted_filenames:
                audioList.append(AudioFileClip(path_name+'/'+num))

            final_audio = concatenate_audioclips(audioList)
            final_audio.write_audiofile(path_name+"/"+doc+".mp3")

            MP3.objects.create(name=path_name.split('/')[-1]+'/'+doc+'.mp3', path=path_name+"/"+doc+".mp3", user=User.objects.get(id=username))
            html.text_to_speech_status = True
            html.save()
            self.send(text_data=json.dumps({'status': 'Combined all the chunks and file is saved in "Mp3 Files" folder.'}))
            self.close()
            # return JsonResponse({'status': 'success'})
        except Exception as e:
            self.send(text_data=json.dumps({'status': 'Something went wrong. Please try again.'}))
            self.close()


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

def get_numeric_part(filename, prefix):
    return int(filename.split(prefix)[1].split('.mp3')[0])

