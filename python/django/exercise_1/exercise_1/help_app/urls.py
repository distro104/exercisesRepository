from django.conf.urls import url
from help_app import views

urlpatterns = [
    url(r'^$', views.help, name='help'),
]
