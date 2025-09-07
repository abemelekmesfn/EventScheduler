from django.db import models
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="organized_events")

    def __str__(self):
        return self.title

class Participant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="participants")
    status = models.CharField(max_length=20, choices=[("Going", "Going"), ("Interested", "Interested"), ("Not Going", "Not Going")])

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"

class Reminder(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reminders")
    reminder_time = models.DateTimeField()

    def __str__(self):
        return f"Reminder for {self.event.title}"
