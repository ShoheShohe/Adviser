from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from pure_pagination.mixins import PaginationMixin

from .models import Attitude
from .forms import AttitudeForm

# Create your views here.


class AttitudeFilterView(LoginRequiredMixin, PaginationMixin, FilterView):
    model = Attitude
    context_object_name = "attitude_list"

    # pure_pagination用設定
    paginate_by = 3
    object = Attitude


class AttitudeDetailView(LoginRequiredMixin, DetailView):
    model = Attitude


class AttitudeCreateView(LoginRequiredMixin, CreateView):
    model = Attitude
    form_class = AttitudeForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.maker = self.request.user
        return super().form_valid(form)


class AttitudeUpdateView(LoginRequiredMixin, UpdateView):
    model = Attitude
    form_class = AttitudeForm
    success_url = reverse_lazy('index')


class AttitudeDeleteView(LoginRequiredMixin, DeleteView):
    model = Attitude
    success_url = reverse_lazy('index')