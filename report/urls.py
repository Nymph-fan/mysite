from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.table, name='table'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^index/', views.index, name='index'),
    url(r'^detail/(?P<asset_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^$', views.dashboard),

]