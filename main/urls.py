from django.urls import path
from main.api_views import ShortURLListCreateView, forwartAPIView


urlpatterns = [
    path('main/',ShortURLListCreateView.as_view(), name="create"),
    path('<str:short_url>/', forwartAPIView.as_view(), name="forward")
]