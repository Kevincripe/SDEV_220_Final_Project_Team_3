from django import forms

from .models import SoldUnits

class SoldForm(forms.ModelForm):

    class Meta:
        model = SoldUnits
        fields = ('Inventory', 'Year_Make_Model','comments')
        