from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime

def homepage(request):
	template = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	html = template.render(locals())
	return  HttpResponse(html)
# Create your views here.
