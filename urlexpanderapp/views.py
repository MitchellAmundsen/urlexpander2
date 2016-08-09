from urllib.request import urlopen
from django.shortcuts import render, get_object_or_404
from .models import URL
from .forms import URLForm
from bs4 import BeautifulSoup
import requests

def url_list(request):
	urls = URL.objects.all()
	return render(request, 'urlexpanderapp/url_list.html', {'urls' : urls})

def url_detail(request, url_pk):
	current = get_object_or_404(URL, pk=url_pk)
	return render(request, 'urlexpanderapp/url_detail.html', {'url' : current})

'''
def urlexpander(request, address):
	if request.method == "POST":
		form = URLForm(request.POST)
		post = form.save(commit=False)
		get = urlopen(form.url_short)
		post.url_short = address
		header = get.getheader()
		post.url_long = header.location
		post.status = get.status
		html = get.read()
		post.title = html.split('<title>')[1].split('</title>')[0]
		post.save()
		return redirect('url_detail', pk=post.pk)
	else:
		form = URLForm()
	return render(request, 'urlexpanderapp/url_new.html', {'urls': url})
'''

def url_add(request):
	shorturl = request.POST['shorturl']
	page = requests.get(shorturl)
	url = URL()
	url.status = page.status_code
	if url.status == 200:
		soup  = BeautifulSoup(page.content)
		url.title = soup.head.title.contents[0]
	else:
		url.title = "None"
	url.url_short = shorturl
	url.url_long = page.url
	url.save()
	return render(request, 'urlexpanderapp/url_detail.html', {'url' : url})

def url_delete(request, url_pk):
	current = get_object_or_404(URL, pk=url_pk)
	current.delete()
	urls = URL.objects.all()
	return render(request, 'urlexpanderapp/url_list.html', {'urls' : urls})


