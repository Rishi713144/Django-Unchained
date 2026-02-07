from django import forms
from .models import newappmodel

class newappForm(forms.ModelForm):
    newapp_model = forms.ModelChoiceField(
        queryset=newappmodel.objects.all(),
        label='Select a Machine',
        empty_label='--- Choose ---'
    )

    class Meta:
        model = newappmodel
        fields = ['newapp_model']
