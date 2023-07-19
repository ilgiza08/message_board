from django.views.generic import ListView, DetailView, CreateView
from .models import Advertisement
from .forms import CreateForm


class AdvertisementView(ListView):
    """Выводит ленту с объявлениями"""
    model = Advertisement
    template_name = 'advertisements.html'
    queryset = Advertisement.objects.order_by('-created')
    paginate_by = 10


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisement.html'
    context_object_name = 'adv'


class AdvertisementCreateView(CreateView):
    form_class = CreateForm
    template_name = 'adv_create.html'
