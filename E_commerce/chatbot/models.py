from django.db import models
from django.contrib.auth.models import User

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_user_message = models.BooleanField(default=True) # True for user, False for bot
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = "Chat Histories"

    def __str__(self):
        return f'{self.user.username}: {self.message[:50]}...'