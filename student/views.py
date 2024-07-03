import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from djangoProject.settings import EMAIL_HOST_USER
from student.filters import StudentFilter
from student.forms import StudentForm, StudentUpdateForm
from student.models import Student, HistoryStudent
from trainer.models import Trainer


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('home')
    permission_required = 'student.add_student'

    def form_valid(self, form):
        if form.is_valid():
            new_student = form.save()
            details_student = {
                'fullname': f'{new_student.first_name} {new_student.last_name}',
            }

            subject = 'Confirmare cont nou!'
            message = get_template('mail.html').render(details_student)
            mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_student.email])
            mail.content_subtype = 'html'
            mail.send()

            history_message = (f"Studentul,{new_student.last_name},{new_student.last_name},"
                               f"a fost create de {self.request.user.username} la data de:{datetime.date.today()}")

            HistoryStudent.objects.create(message=history_message, created_at=datetime.datetime.now(),
                                          user=User.objects.get(id=self.request.user.id), active=True)

        return super().form_valid(form)


class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = "all_students"
    permission_required = 'student.can_view_list_of_students'

    def get_queryset(self):
        return Student.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        students = Student.objects.filter(active=True)
        my_filters = StudentFilter(self.request.GET, queryset=students)
        context['all_students'] = my_filters.qs
        context['form_filters'] = my_filters.form

        return context


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('students-list')
    permission_required = 'student.change_student'


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = "student/delete_student.html"
    model = Student
    success_url = reverse_lazy('students-list')
    permission_required = 'student.delete_student'


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = "student/details_student.html"
    model = Student
    permission_required = 'student.view_student'


    # Metoda get_context_data este folosita in clasele de view cum ar fi DetailView, CreateView, DeleteView, ListView, TemplateView etc.
    # Aceasta metoda este folosita pentru a furniza date suplimentare catre template-ul asociat view-lui.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        now = datetime.datetime.now()
        context['current_datetime'] = now

        context['students'] = Student.objects.all()
        context['trainers'] = Trainer.objects.all()

        print(context)

        return context


class HistoryStudentListView(ListView):
    model = HistoryStudent
    template_name = 'student/history_student.html'
    context_object_name = 'history_list'

    def get_queryset(self):
        return HistoryStudent.objects.filter(user=User.objects.get(id=self.request.user.id))
