from django.shortcuts import render_to_response , get_object_or_404
from imghost.models import Picture
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
import time 
from django.core.paginator import Paginator, InvalidPage, EmptyPage



def index2(request):

    latest_picture = Picture.objects.latest('id')

    return render_to_response('index.html', {'latest_picture': latest_picture, },context_instance=RequestContext(request))

def picture_detail(request,picture_id):

    latest_picture = get_object_or_404(Picture, id=picture_id)
    return render_to_response('image_detail.html', {'picture': latest_picture})
    
def upload(request):
    if "file" in request.FILES:
        filename=str(int(time.time())) + "." + request.FILES["file"].name.split(".")[-1]
        picture=Picture()
        picture.image.save(filename,request.FILES["file"])
        return HttpResponseRedirect(reverse('imghost.views.picture_detail', args=[picture.id]))
    return HttpResponseRedirect(reverse('imghost.views.index', args=[]))

def index(request):
    pictures_list = Picture.objects.all()
    paginator = Paginator(pictures_list, 3)  #Show 25 contacts per page
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        pictures_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pictures_page = paginator.page(paginator.num_pages)
        
    return render_to_response('index.html', {"pictures_page": pictures_page},context_instance=RequestContext(request))

        
