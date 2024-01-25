from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect,Http404
from .models import Shortner
from .forms import ShortnerFrom


# Create your views here.

def home_view(request):
    template='home.html'
    context={}
    context['form']=ShortnerFrom
    
    if request.method=='GET':
         return render(request, template, context)
        
    
    elif request.method=='POST':
        used_form=ShortnerFrom(request.POST)
        if used_form.is_valid():
            
            shortend_object=used_form.save()
            
            new_url=request.build_absolute_uri('/')+shortend_object.short_url   #build_absolute_uri this for using customize uri
            
            #print(request.build_absolute_uri())
            
            long_url=shortend_object.long_url
            
            context['new_url']=new_url
            context['long_url']=long_url
            context['short_code']=shortend_object.short_url
            
            return render(request,template,context)
        
        context['errors']=used_form.errors
        return render(request,template,context)

def redirect_url_view(request,shortened_part):
    if shortened_part=='admin':
        return admin.site.urls
    
    try:
        shortner=Shortner.objects.get(short_url=shortened_part)
        shortner.time_followed+=1
        shortner.save()
        return HttpResponseRedirect(shortner.long_url)
    
    except Shortner.DoesNotExist:
        raise Http404('Sorry,this link is broken:')
    