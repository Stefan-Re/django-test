from django.db import models


class Trainer(models.Model):

    department_choice = {
        ("b", 'Backend'),
        ("f", 'Frontend'),
        ("n", 'Network'),
    }

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    active = models.BooleanField(default=True)
    department = models.CharField(max_length=20, choices=department_choice, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'