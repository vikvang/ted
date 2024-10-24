from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ButtonPress, SpeechSimulation

@csrf_exempt
def simulate_button_press(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        button_id = data.get('button_id')
        message = f'Button {button_id} pressed'
        # Save to the database
        ButtonPress.objects.create(button_id=button_id, message=message)
        return JsonResponse({'message': message})

@csrf_exempt
def simulate_speech(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text')
        response = f'Teddy says: {text}'
        # Save to the database
        SpeechSimulation.objects.create(text=text, response=response)
        return JsonResponse({'message': response})