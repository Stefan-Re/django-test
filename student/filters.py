import django_filters
from django import forms

from student.models import Student
from trainer.models import Trainer


# lookup_expr: icontains, startswith, endswith, exact, lte, lt, gte, gt

# lte - less than or equal to
# lt - less than
# gte - greater than or equal to
# gt - greater than


class StudentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains', label="First name", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Search first name'}))
    last_name = django_filters.CharFilter(lookup_expr='icontains', label="Last name", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Search last name'}))


    #age = django_filters.NumberFilter(lookup_expr='icontains', label="Age", widget=forms.NumberInput(
    #    attrs={'class': 'form-control', 'placeholder': 'Search age'}))

    list_ages = [(i, i) for i in range(18,30 +1)]
    age = django_filters.ChoiceFilter(choices=list_ages, widget=forms.Select(attrs={'class': 'form-select'}))



    #trainer = django_filters.ChoiceFilter(
    #    choices=[(trainer.id, trainer) for trainer in Trainer.objects.filter(active=True)],
    #    widget=forms.Select(attrs={'class': 'form-select'}))

    trainer = django_filters.ChoiceFilter(
        choices=[(trainer.id, trainer) for trainer in Trainer.objects.filter(active=True)],
        widget=forms.RadioSelect(attrs={}))


    start_date_gte = django_filters.DateFilter(field_name='start_date', lookup_expr='gte', label="From start date",
                                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    start_date_lte = django_filters.DateFilter(field_name='start_date', lookup_expr='lte', label="To start date",
                                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    end_date_gte = django_filters.DateFilter(field_name='end_date', lookup_expr='gte', label="From end date",
                                             widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date_lte = django_filters.DateFilter(field_name='end_date', lookup_expr='lte', label="To end date",
                                             widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'trainer', 'start_date_gte', 'start_date_lte',
                  'end_date_lte',
                  'end_date_gte']