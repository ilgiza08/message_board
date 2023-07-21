from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Advertisement
from .forms import CreateAdvForm, CommentForm
from django.urls import reverse


class AdvertisementView(ListView):
    """Выводит ленту с объявлениями"""
    model = Advertisement
    template_name = 'advertisements.html'
    queryset = Advertisement.objects.order_by('-created')
    paginate_by = 10


class AdvertisementDetailView(DetailView):
    """Выводит детали об объявлении"""
    model = Advertisement
    template_name = 'advertisement.html'
    context_object_name = 'adv'


class AdvertisementCreateView(CreateView):
    """Создать объявление"""
    form_class = CreateAdvForm
    template_name = 'adv_create.html'

    def get_success_url(self):
        return reverse('advertisement', kwargs={'pk': self.object.pk})
    

class AdvertisementUpdateView(UpdateView):
    """Редактировать объявление"""
    form_class = CreateAdvForm
    template_name = 'adv_create.html'
    
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Advertisement.objects.get(pk=id)

    def get_success_url(self):
        return reverse('advertisement', kwargs={'pk': self.object.pk})
    

class AddCommentView(CreateView):
    form_class = CommentForm
    template_name = 'advertisement.html'
