from typing import Any, Dict
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Advertisement
from .forms import CreateAdvForm, CommentForm
from django.urls import reverse
from django.shortcuts import redirect


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = self.request.user
            form.advertisement_id = self.kwargs['pk']
            form.save()
        else:
            form = CommentForm()
        return super().get(request, *args, **kwargs)


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
    

# class AddCommentView(CreateView):
#     template_name = 'advertisement.html'
#     form_class = CommentForm
    
#     def form_valid(self, form):
#         instance = form.save(commit=False)
#         instance.author = self.request.user
#         instance.save() 
#         return redirect('/advertisement/')