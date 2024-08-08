from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    ETFO=TopicForms() # ETFO - insert topic form object 
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForms(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topicname']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()2
            return HttpResponse('Topic is created')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topicname']
            na=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']

            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
            WO.save()
            return HttpResponse('Webpage is Created')

    return render(request,'insert_webpage.html',d)