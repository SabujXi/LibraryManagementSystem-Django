from django.forms import Form
from django import forms


class MemberForm(Form):
    name = forms.CharField(min_length=10, max_length=20, required=True, strip=True)
    email = forms.EmailField(required=False)
    bio = forms.CharField(max_length=100000, required=False, strip=True)




