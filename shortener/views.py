from django.shortcuts import render
from django.http import HttpResponse

import uuid

from .models import Url


# Create your views here.
def base(request):
    new_urls = Url.objects.all()
    ctx = {
        'urls': new_urls
    }
    return render(request, 'base.html', context=ctx)


def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]  # generate unique id of length 5
        new_url = Url(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(f'https://{url_details.link}')
