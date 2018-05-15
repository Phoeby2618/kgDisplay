
from django.urls import path,re_path

from . import views

app_name='display'

urlpatterns = [

    # re_path(r'^test/(?P<drug_id>[0-9]+)$', views.druginfo, name='drug_page'),
    # path('test/',views.index),
    path('info/',views.symptom),
    path('Prof/',views.display),
    path('look/',views.looks,name='look'),
    path('test/',views.testclick,name='testclick'),

    path('form/',views.formpost),
    path('add/',views.add,name='add'),

]