from django.views.generic import ListView, DetailView
from .models import Advertisement


class AdvertisementView(ListView):
    """Выводит ленту с объявлениями"""
    model = Advertisement
    template_name = 'advertisements.html'
    queryset = Advertisement.objects.all()


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisement.html'
    context_objects_name = 'advertisement'

