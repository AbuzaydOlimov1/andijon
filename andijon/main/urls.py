from django.urls import path
from .views import *


urlpatterns = [
    path('get-banner/', get_banner),
    path('get-all/', get_all),
    path('get-option/', get_option),
    path('get-all-offer/', get_all_offer),
    path('get-special/', get_special),
    path('get-builder/', get_builder),
    path('get-single/<int:pk>', get_single),
    path('get-about/', get_about),
    path('get-service/', get_service),
    path('get-about-broker/', get_about_broker),
    path('get-broker/', get_broker),
    path('get-step/', get_step),
    path('get-option/', get_option),
    path('get-bid/', get_bid),
    path('set-bid/', set_bid),
]