from django.views.generic import ListView
from .models import Advertisement


class AdvertisementView(ListView):
    model = Advertisement
    template_name = 'advertisements.html'
    context_objects_name = 'advertisements'
    queryset = Advertisement.objects.order_by('-created')
    paginate_by = 10


class AdvertisementDetailView():
    model = Advertisement
    template_name = 'advertisement.html'
    context_objects_name = 'advertisement'