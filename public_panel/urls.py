from django.urls import path
from .views import HomePageView

app_name = 'public_panel'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
]
