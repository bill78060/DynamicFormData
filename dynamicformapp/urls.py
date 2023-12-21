from django.urls import path
from .views import dynamic_form_view, success_view

urlpatterns = [
    path('', dynamic_form_view, name='dynamic_form_view'),
    path('success/', success_view, name='success_view'),

    # path('dynamic_form/', dynamic_form_view, name='dynamic_form'),
    # Add other URLs as needed
]

