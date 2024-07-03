from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.models import Student
from trainer.filters import TrainerFilter
from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer


class TrainerCreateView(LoginRequiredMixin, CreateView):
    template_name = "trainer/create_trainer.html"
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('home')


class TrainerListView(LoginRequiredMixin, ListView):
    template_name = "trainer/list_of_trainers.html"
    model = Trainer
    context_object_name = "all_trainers"

    def get_queryset(self):
        return Trainer.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        trainers = Trainer.objects.filter(active=True)
        my_filters = TrainerFilter(self.request.GET, queryset=trainers)
        context['all_trainers'] = my_filters.qs
        context['form_filters'] = my_filters.form

        return context


class TrainerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm
    success_url = reverse_lazy('trainer-list')


class TrainerDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('trainer-list')


class TrainerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'trainer/details_trainer.html'
    model = Trainer

#def trainer_show_students(request, trainer_id):
#    trainer = Trainer.objects.get(pk=trainer_id)
#    students = trainer.objects.get.all


def get_all_students_per_trainer(request, pk):
    get_students = {'get_students': Student.objects.filter(trainer_id=pk)}

    return render(request, 'trainer/get_all_students_per_trainer.html', get_students)

