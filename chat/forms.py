
from user.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic',)