from django import forms


class AddressForm(forms.Form):
    street = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    state = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    zip = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    country = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
