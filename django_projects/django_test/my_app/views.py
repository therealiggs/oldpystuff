from django.shortcuts import render
from .models import Post

def index(request):
	return render(request, "main.html", context={'post': Post.objects.latest(field_name='post_date')})
