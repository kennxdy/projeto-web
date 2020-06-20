import os

from django.shortcuts import render
from django.http import FileResponse, Http404

from .models import Contact


def index(request):
    try:
        contato = Contact.objects.all()
        context = {'contato': contato[0]}
        return render(request, 'singlepage/index.html', context)
    except:
        return render(request, 'singlepage/index.html')


def download_matriz(request):
    dir_name = os.path.join(os.getcwd(), 'singlepage', 'documents')
    file_name = 'matriz.odt'
    file_path = os.path.join(dir_name, file_name)

    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'))
    raise Http404
