import socket

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.urls import reverse


def index(request):
    if request.method == 'POST':
        res, picname = handleFile(request.FILES["testName"])
        if res == 'problem occurred during reconstruction':
            res = None


        return HttpResponseRedirect('modelEval?res=%s&picname=%s' % (res, picname))

    context = dict()

    res = request.GET.get('res', False)
    if res is False:
        context['greetings'] = 'drop a picture to get an 3d model'
    elif res == "None":
        context['greetings'] = 'sorry, last conversion failed'
    else:
        context['greetings'] = 'Your result here:'
        context['res'] = res
        context['picname'] = request.GET.get('picname', False)

    template = loader.get_template('modelEval/index.html')

    return HttpResponse(template.render(context, request))


def handleFile(f):
    fs = FileSystemStorage()
    filename = fs.save(f.name, f)

    uploaded_file_url = fs.url(filename)
    print(uploaded_file_url)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 12345

    host_ip = 'localhost'

    s.connect((host_ip, port))

    s.send(uploaded_file_url.encode('utf-8'))

    res = s.recv(1024).decode('utf-8')
    s.close()
    return res, filename
