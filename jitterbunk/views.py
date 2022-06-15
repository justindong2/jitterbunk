from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import User, Bunk

# Create your views here.
def index(request):
    bunks = Bunk.objects.all()
    return render(request, 'jitterbunk/index.html', {'bunks': bunks})

def personal(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    bunks = Bunk.objects.filter(to_user__id=user_id)
    return render(request, 'jitterbunk/personal.html', {'user': user, 'bunks': bunks})

def sendbunk(request):
    return render(request, 'jitterbunk/sendbunk.html')

def postbunk(request):
    try:
        from_user = User.objects.get(username=request.POST['from'])
        to_user = User.objects.get(username=request.POST['to'])
    except (KeyError, User.DoesNotExist):
        return render(request, 'jitterbunk/sendbunk.html')
    else:
        newbunk = Bunk(from_user=from_user, to_user=to_user, time=timezone.now())
        newbunk.save()
        return HttpResponseRedirect(reverse('jitterbunk:personal', args=(to_user.id,)))