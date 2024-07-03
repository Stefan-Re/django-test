from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from feedback.models import Feedback
from feedback.forms import FeedbackForm

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    template_name = 'feedback/create_feedback.html'
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy("home")

class FeedbackListView(LoginRequiredMixin, ListView):
    template_name = 'feedback/list_of_feedback.html'
    model = Feedback
    context_object_name = 'feedback_list'