from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreatinForm(UserCreationForm):
    class Meta:
        model = CustomUser
        feilds = UserCreationForm.Meta.fields
        
class CustomUserChangeForm(UserChangeForm):
    class Meta :
        model = CustomUser
        feilds = UserChangeForm.Meta.Feilds
        
        