from django import forms

from .models import SalesLead

class SalesForm(forms.ModelForm):

    class Meta:
        model = SalesLead
        fields = ('first_name', 'last_name','street_address', 'city','state', 'zipcode','telephone', 'comments')
        