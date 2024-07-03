from django.contrib.auth.models import User
from django.db import models
from trainer.models import Trainer


class Student(models.Model):
    gender_options = {
        ('M', 'Male'),
        ('F', 'Female'),
    }

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=500)
    active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()
    gender = models.CharField(max_length=1, choices=gender_options)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(
        auto_now_add=True)  # stocam data si ora la salvarea unui student. Nu se mai modifica data si ora
    updated_at = models.DateTimeField(auto_now=True)  # stocam data si ora la orice modificare in clasa student

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    price = models.IntegerField(null=True)


class HistoryStudent(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message