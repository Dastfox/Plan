from django import forms


class NewUrlForm(forms.Form):
    NewUrl = forms.URLField(label='New Url', max_length=2300)
    