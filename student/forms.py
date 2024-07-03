from django import forms

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'trainer': forms.Select(attrs={'class': 'form-select'}),
        }

    # Metoda clean este folosita pentru a verifica corectitudinea datelor introduse. Atunci cand implmmentam un formular
    # trebuie sa realizam validari personalizate care sa se aplice pe intregul formular

    def clean(self):
        cleaned_data = super().clean()

        # O validare prin care verificam unicitatea adresei de email. Daca am student cu o adresa de email sa nu pot adauga un alt student cu aceeasi de email
        get_email = cleaned_data.get('email')  # accesam valoarea cheii email din dictionarul cleaned_data
        check_emails = Student.objects.filter(
            email=get_email)  # interogam tabela student_student cautand in coloana email daca exista adresa de email stocata in variabila get_email
        if check_emails:  # verificam daca exista vreun student cu aceeasi adresa de email stocata in tabela
            msg = 'Email already registered'  # mesajul ce va afisat pe ecran
            self.add_error('email', msg)  # adaugarea erorii pe campul email cu mesajul stocat in variabiala msg.

        # O validare in care verificati daca start_date este mai mare decat end_date sa nu il lasati pe utilizator sa salveze inregistrarea

        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date > end_date:
            msg = 'Start date must be before end date'
            self.add_error('start_date', msg)

        # O validare in care sa verificati daca exista un student in baza de date cu acelasi first_name SI last_name.

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        check_first_and_last_name = Student.objects.filter(first_name=first_name, last_name=last_name)
        if check_first_and_last_name:
            msg = 'The first and last name are already registered'
            self.add_error('first_name', msg)

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'trainer': forms.Select(attrs={'class': 'form-select'}),
        }
