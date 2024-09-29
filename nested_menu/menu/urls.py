from django.urls import path

from .views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<str:item_url>", IndexView.as_view(), name="index"),
]
