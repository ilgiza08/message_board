from django.urls import path
from .views import AdvertisementView, AdvertisementDetailView
from .views import AdvertisementCreateView, AdvertisementUpdateView, CreateCommentView


urlpatterns = [
    path('', AdvertisementView.as_view(), name='main'),
    path('<int:pk>', AdvertisementDetailView.as_view(), name='advertisement'),
    path('create/', AdvertisementCreateView.as_view(), name='adv_create'),
    path('update/<int:pk>/', AdvertisementUpdateView.as_view(), name='update'),
    path('<int:pk>/comment/', CreateCommentView.as_view(), name='comment'),
]