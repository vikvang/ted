from django.db import models

class ButtonPress(models.Model):
    button_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)

class SpeechSimulation(models.Model):
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    response = models.CharField(max_length=255)