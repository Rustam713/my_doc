from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):

    articles = Article.objects.all()



    return render(request, template_name='app/index.html', context={'articles': articles})

def detail(request, pk):
    article = Article.objects.get(pk=pk)

    return render(request, template_name='app/detail.html', context={'article': article})








