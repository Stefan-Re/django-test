from django.contrib import admin

from student.models import Student, Book


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age',)
    search_fields = ('first_name', 'last_name', 'email', 'age',)


@admin.register(Book)
class StudentBook(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price')
    search_fields = ('title', 'author')