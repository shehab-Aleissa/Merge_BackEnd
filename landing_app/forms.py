from django import forms
from app.models import GetingUsersEmails


class UserEmailForm(forms.ModelForm):
    class Meta:
        model = GetingUsersEmails
        fields = '__all__'

