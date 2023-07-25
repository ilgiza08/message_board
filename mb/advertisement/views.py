from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Advertisement, Comment
from .forms import CreateAdvForm, CommentForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class AdvertisementView(ListView):
    """Выводит ленту с объявлениями"""
    model = Advertisement
    template_name = 'advertisements.html'
    paginate_by = 10

    def get_queryset(self):
        return Advertisement.objects.order_by('-created').select_related('author')


class AdvertisementDetailView(DetailView):
    """Выводит детали об объявлении"""
    model = Advertisement
    template_name = 'advertisement.html'
    context_object_name = 'adv'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(advertisement=self.object.pk).select_related('author')
        return context


class SetAuthorMixin(LoginRequiredMixin):
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdvertisementCreateView(SetAuthorMixin, CreateView):
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
    

class CreateCommentView(SetAuthorMixin, CreateView):
    """Добавить комментарий"""
    form_class = CommentForm
    success_url = '/advertisement/'
    
    def form_valid(self, form):
        form.instance.advertisement_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs):
        return reverse('advertisement', kwargs={'pk': self.kwargs['pk']})
    

class CommentView(LoginRequiredMixin, ListView):
    """Показывает все отклики к моим объявлениям"""
    model = Comment
    template_name = 'all_comments.html'

    def get_queryset(self):
        return Comment.objects.filter(advertisement__author=self.request.user).select_related('author', 'advertisement')


def comment_delete(request, pk):
    """Удалить отклик"""
    comment = Comment.objects.get(id=pk)
    if comment:
        comment.delete()
    return redirect('all_comments')


def comment_accept(request, pk):
    """Принять отклик"""
    comment = Comment.objects.get(id=pk)
    if comment:
        print(comment)
    return redirect('all_comments')