from django import forms

class searchform(forms.Form):
    search=forms.CharField( required=False,label='')
