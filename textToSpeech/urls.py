from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('media/<path:path>', media_files, name="secure"),
    path('html', html, name="html"),
    path('mp3', mp3, name="mp3"),
    # path('summary', summary, name="summary"),
    path('public', public, name="public"),
    path('text-files', textfiles, name="text-files"),
    path('convert_to_mp3', convert_to_mp3, name="convert_to_mp3"),
    path('move_to_public', move_to_public, name="move_to_public"),
    path('pdfitem', pdfListView.as_view(), name="pdfitem"),
    path('epubitem', epubListView.as_view(), name="epubitem"),
    path('htmlitem', htmlListView.as_view(), name="htmlitem"),
    path('mp3item', mp3ListView.as_view(), name="mp3item"),
    path('summaryitem', summaryListView.as_view(), name="summaryitem"),
    path('publicfileitem', publicFileListView.as_view(), name="publicfileitem"),
    path('textfilesitem', textFileListView.as_view(), name="publicfileitem"),
    path('savepdf', savepdf, name="savepdf"),
    path('savetext', savetext, name="savetext"),
    path('pdftohtmlandtext', pdftohtmlandtext, name="pdftohtmlandtext"),
    path('get_length_of_txt_file', get_length_of_txt_file, name="get_length_of_txt_file"),
    path('divide_chunks', divide_chunks, name="divide_chunks"),
    path('create_summmary', createsummmary, name="create_summmary"),
    path('delete_pdf_file/<int:id>', delete_pdf, name="delete_pdf"),
    path('delete_text_file/<int:id>', delete_text, name="delete_text"),
    path('delete_epub_file/<int:id>', delete_epub, name="delete_epub"),
    path('delete_html_file/<int:id>', delete_html_file, name="delete_html_file"),
    path('delete_mp3_file/<int:id>', delete_mp3_file, name="delete_mp3_file"),
    path('delete_summary_file/<int:id>', delete_summary_file, name="delete_summary_file"),
    path('delete_public_file/<int:id>', delete_public_file, name="delete_public_file"),
    path('rename_text_files_path/', rename_text_files_path, name="rename_text_files_path"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
