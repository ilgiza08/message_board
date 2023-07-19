from django.forms import ModelForm
from .models import Advertisement
 

class CreateForm(ModelForm):
    """Форма создания объявления"""

    class Meta:
        model = Advertisement
        fields = [
            'title', 'text', 'image', 'video', 'files', 
            'category', 'author',
            ]