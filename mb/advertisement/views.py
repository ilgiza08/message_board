from django.views.generic import ListView, DetailView
from .models import Advertisement, Comment


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
