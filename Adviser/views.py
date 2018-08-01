from datetime import timedelta

import subprocess
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
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

    def get_queryset(self):
        return Attitude.objects.filter(maker=self.request.user).order_by('practiced_rate')
    # ひとまずデフォルトは成功率の低いものから順に表示するようにしているが、のちに変更すべき。

    # pure_pagination用設定
    paginate_by = 3
    object = Attitude

    def post(self, request):
        if request.POST:
            rated_attitude = Attitude.objects.get(pk=request.POST['attitude.pk'])
            rated_attitude.timing += 1
            rated_attitude.frequency = rated_attitude.timing / (timezone.now() - rated_attitude.adopted_date).days
            rated_attitude.total_succeeded_point += int(request.POST['star'])
            rated_attitude.practiced_rate = rated_attitude.total_succeeded_point / (rated_attitude.timing * 5)
            rated_attitude.save()
            # 更新できた旨のお知らせと、星をまた灰色に戻す
            subprocess.getoutput('../static/Adviser/js/message.js')
        else:
            pass
        return HttpResponseRedirect(reverse_lazy('index'))


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