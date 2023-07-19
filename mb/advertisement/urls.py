from django.urls import path
from .views import AdvertisementView, AdvertisementDetailView, AdvertisementCreateView


urlpatterns = [
    path('', AdvertisementView.as_view()),
    path('<int:pk>', AdvertisementDetailView.as_view(), name='advertisement'),
    path('create/', AdvertisementCreateView.as_view(), name='adv_create'),
    # path('update/<int:pk>', Advertisements.as_view()),
    # path('comments/', ),
]