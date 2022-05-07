from .models import Category
from django import forms

CHOICES = [('ALL', 'ALL')] + [(i.title, i.title) for i in Category.objects.all()]


class APIForm(forms.Form):
    category = forms.ChoiceField(choices=CHOICES)
    title = forms.CharField(initial='Lenovo')
    limit = forms.IntegerField(initial=5, max_value=15, min_value=1)

