from datetime import timedelta

import subprocess
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django_filters.views import FilterView
from pure_pagination.mixins import PaginationMixin

from .models import Attitude
from .filters import AttitudeFilter
from .forms import AttitudeForm

# Create your views here.


class AttitudeFilterView(LoginRequiredMixin, PaginationMixin, FilterView):
    model = Attitude
    filterset_class = AttitudeFilter
    context_object_name = "attitude_list"

    def get_queryset(self):
        user_attitudes = Attitude.objects.filter(maker=self.request.user)
        return user_attitudes.order_by((F('frequency') * (1 - F('practiced_rate'))).desc())
    # ひとまずデフォルトは成功率の低いものから順に表示するようにしているが、のちに変更すべき。

    # pure_pagination用設定
    paginate_by = 3
    object = Attitude

    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]
        return super().get(request, **kwargs)

    def post(self, request):
        if request.POST:
            rated_attitude = Attitude.objects.get(pk=request.POST['attitude.pk'])
            rated_attitude.timing += 1
            rated_attitude.frequency = rated_attitude.timing / (timezone.now() - rated_attitude.adopted_date).days
            rated_attitude.total_succeeded_point += int(request.POST['star'])
            rated_attitude.practiced_rate = rated_attitude.total_succeeded_point / (rated_attitude.timing * 5)
            rated_attitude.save()
            # 更新できた旨のお知らせと、星をまた灰色に戻す
            messages.success(request,
                             '''心がけ:「{0}」の、
                             認識すべきだった回数を+1, 
                             成功ポイントを+{1}しました。'''.format(rated_attitude.declaration, request.POST['star']))
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