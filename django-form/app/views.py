from django.shortcuts import render, redirect
from .forms import FeedbackForm

# Create your views here.



def add_into(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'feedback_from': form})
