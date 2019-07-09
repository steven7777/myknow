from django import forms

from .models import Entity

class EntityCompareForm(forms.ModelForm):

    class Meta:
        model = Entity
        fields = ('name', 'name', 'perso',)
