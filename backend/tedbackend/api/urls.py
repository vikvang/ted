from django.urls import path
from . import views

urlpatterns = [
    path('simulate-button/', views.simulate_button_press, name='simulate_button_press'),
    path('simulate-speech/', views.simulate_speech, name='simulate_speech'),
]