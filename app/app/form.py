from django import forms


class Userform(forms.Form):
    name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
