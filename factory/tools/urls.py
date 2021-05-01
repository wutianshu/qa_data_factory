from django.urls import path
from .views.common import get_idcards, addPromotion,getPromotion
from .views.eenum import get_region, get_type, get_resource

urlpatterns = [
    path('idcards/', get_idcards, name='idcards'),
    path('region/', get_region, name='get_region'),
    path('type/', get_type, name='get_type'),
    path('resource/', get_resource, name='get_resource'),
    path('addPromotion/', addPromotion, name='addPromotion'),
    path('getPromotion/', getPromotion, name='getPromotion'),
]
