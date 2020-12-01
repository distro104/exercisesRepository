from django.conf.urls import url
from exercise_1_app import views

urlpatterns = {
    url(r'^$', views.index, name='index'),
}
