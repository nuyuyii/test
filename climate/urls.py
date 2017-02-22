from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.conctrat_page, name='map'),
    url(r'^data_ltln', views.data_ltln, name='data_ltln'),
]
