from django import forms

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'course_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'department' : forms.Select(attrs={'class': 'form-select'}),
        }


class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'course_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'department' : forms.Select(attrs={'class': 'form-select'}),
        }