import django_filters
from django import forms
from trainer.models import Trainer


class TrainerFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains', label="First name", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Search first name'}))
    last_name = django_filters.CharFilter(lookup_expr='icontains', label="Last name", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Search last name'}))
    department = django_filters.ChoiceFilter(choices=Trainer.department_choice, label="Department",
                                             widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'department']
