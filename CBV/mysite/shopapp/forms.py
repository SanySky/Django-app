from django import forms
from django.contrib.auth.models import Group
from django.forms import ModelForm
from .models import Order


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name"]


#from django.core import validators


#class ProductForm(forms.Form):
#    name = forms.CharField(max_length=100)
#    price = forms.DecimalField(min_value=1, max_value=1000000, decimal_places=2)
#    description = forms.CharField(
#        label="Product description",
#        widget=forms.Textarea(attrs={"rows": 5, "cols": 30}),
#       validators=[validators.RegexValidator(
#            regex="great",
#            message="Field mast contain word 'great'"
#        )],
#    )

