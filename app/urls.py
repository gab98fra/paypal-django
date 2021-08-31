from django.urls import path
from .views import TemplatePayView, PayView

app_name="home"
urlpatterns = [
    path('', TemplatePayView.as_view(), name="home"),
    path('pay/', PayView.as_view(), name="pay"),
]


