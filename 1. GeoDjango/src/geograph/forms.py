from django import forms

class step1(forms.Form):
    Prenom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Nom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))

class step2(forms.Form):
    Adresse = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Code_postal = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Ville = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class' : 'form-control'}))