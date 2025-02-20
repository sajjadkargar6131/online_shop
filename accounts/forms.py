from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreatinForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
        
class CustomUserChangeForm(UserChangeForm):
    class Meta :
        model = get_user_model()
        fields = UserChangeForm.Meta.fields
        