from django.shortcuts import render
from django.views.generic import ListView
from .models import SinglePod

def index(request):
    single_pods = SinglePod.objects.all()

    return render(request, template_name='app/index.html', context={'single_pods': single_pods})



class IndexList(ListView):
    model = SinglePod
    template_engine = 'app/index.html'
    context_object_name = 'single_pods'
    paginate_by = 10
