from django import forms
from accounts.models import accountholder
from accounts.models import banktype
from accounts.models import amounttype

class accountModelForm(forms.ModelForm):
    class Meta:
        model = accountholder
        fields = '__all__'

class depositModelForm(forms.ModelForm):
    class Meta:
        model = banktype
        fields = '__all__'

class amountModelForm(forms.ModelForm):
    class Meta:
        model = amounttype
        fields = '__all__'