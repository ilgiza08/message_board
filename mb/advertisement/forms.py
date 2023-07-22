from django.forms import ModelForm
from .models import Advertisement, Comment
from django import forms


class CreateAdvForm(ModelForm):
  """Форма создания объявления"""
  class Meta:
      model = Advertisement
      fields = ['title', 'text',
                'image', 'video',
                'files', 'category', 'author'
              ]
      labels = {
            'title': ('Название'),
            'text': ('Текст объявления'),
            'author': ('Автор'),
            'image': ('Изображение'),
            'video': ('Видео'),
            'files': ('Файлы'),
            'category': ('Категория'),
      }
      widgets = {
          'title': forms.TextInput(attrs={
          'class': 'form-control',
          'placeholder': 'Введите название'
           }),
           'text': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите текст объявления'
       }),
     }
       

class CommentForm(forms.ModelForm):
    """Форма создания комментария"""
    class Meta:
        model = Comment
        fields = ['text', ]