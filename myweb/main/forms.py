from django import forms

class InputName(forms.Form):
    name = forms.CharField(label="Business Name: ", max_length=100)    
