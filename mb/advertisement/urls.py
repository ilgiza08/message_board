from django.urls import path
from .views import AdvertisementView, AdvertisementDetailView
from .views import AdvertisementCreateView, AdvertisementUpdateView


urlpatterns = [
    path('', AdvertisementView.as_view(), name='main'),
    path('<int:pk>', AdvertisementDetailView.as_view(), name='advertisement'),
    path('create/', AdvertisementCreateView.as_view(), name='adv_create'),
    path('update/<int:pk>/', AdvertisementUpdateView.as_view(), name='update'),
    # path('add-comment/', AddCommentView.as_view(), name='add_comment'),
]