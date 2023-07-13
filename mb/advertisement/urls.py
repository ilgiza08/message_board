from django.urls import path
from .views import AdvertisementView, AdvertisementDetailView


urlpatterns = [
    path('', AdvertisementView.as_view(), name='advertisements'),
    path('<int:pk>', AdvertisementDetailView.as_view(), name='advertisement'),
    # path('create/', Advertisements.as_view()),
    # path('update/<int:pk>', Advertisements.as_view()),
    # path('comments/', ),
]