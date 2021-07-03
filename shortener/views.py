from django.shortcuts import render, redirect
from django.http import HttpResponse

import uuid

from .models import Url, UserUrl


# Create your views here.
def base(request):
    new_urls = Url.objects.all()
    total_links = [i+1 for i in range(new_urls.count())]
    ctx = {
        'urls': new_urls,
        'sl': iter(total_links),
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
    link = url_details.link
    if link[:8] == 'https://' or link[:7] == 'http://':
        return redirect(link)
    else:
        return redirect(f'https://{url_details.link}')


def create_user_url(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user # fetch user obj from request
            url = request.POST['link']
            uid = str(uuid.uuid4())[:5]  # generate unique id of length 5
            new_url = UserUrl(user=user, link=url, uuid=uid)
            new_url.save()
            return HttpResponse(uid)


def about(request):
    return render(request, 'about.html')
