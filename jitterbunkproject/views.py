from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('jitterbunk:index'))
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})