from django.shortcuts import render

# api/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def simulate_button_press(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        button_id = data.get('button_id')
        # Simulate hardware response
        response = f"Button {button_id} pressed"
        return JsonResponse({"message": response})

@csrf_exempt
def simulate_speech(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text')
        # Simulate speech processing
        response = f"Teddy says: {text}"
        return JsonResponse({"message": response})
