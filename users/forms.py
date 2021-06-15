from django.forms import fields
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
         # extra columns should be added in the contcatenated tuple
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'age',
        )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'age',
        )