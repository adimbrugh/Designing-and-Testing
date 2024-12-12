from django.db import models

# Create your models here.


from django.contrib.auth import get_user_model
from django.utils.timezone import now


User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    max_attendees = models.PositiveIntegerField(blank=True, null=True)
    attendees = models.ManyToManyField(User, related_name='attended_events', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def is_upcoming(self):
        return self.date > now()
    
    class Meta:
        ordering = ['date']