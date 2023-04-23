from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User, Message
from django.db.models import Q
from django.shortcuts import redirect
import json
from .forms import UserProfileForm
from user.models import Profile

@login_required
def homepage(request):
    users = User.objects.all()
    return render(request, 'homepage.html', {'users': users})

@login_required
def chatroom(request, pk:int):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(
            Q(receiver=request.user, sender=other_user)
         )
    following_users = list(request.user.profile.following.all())
    messages.update(seen=True)
    messages = messages | Message.objects.filter(Q(receiver=other_user, sender=request.user) )
    return render(request, "chatroom1.html", {"other_user": other_user, 'users': User.objects.all(), "user_messages": messages, 'followed_user' : following_users, 'non_followed_user': request.user.profile.non_followed_user})


@login_required
def ajax_load_messages(request, pk):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(seen=False, receiver=request.user)
    
    print("messages")
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "sent": message.sender == request.user,
        #"picture": other_user.profile.picture.url,

        "date_created": naturaltime(message.date_created),

    } for message in messages]
    messages.update(seen=True)
    
    if request.method == "POST":
        message = json.loads(request.body)['message']
        
        m = Message.objects.create(receiver=other_user, sender=request.user, message=message)
        message_list.append({
            "sender": request.user.username,
            "username": request.user.username,
            "message": m.message,
            "date_created": naturaltime(m.date_created),

           # "picture": request.user.profile.picture.url,
            "sent": True,
        })
    print(message_list)
    return JsonResponse(message_list, safe=False)
def video(request):
    return render(request,'video.html')
