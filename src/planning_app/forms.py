from django import forms

class SendForm(forms.Form):
    Send = forms.BooleanField(label='button', default = False)