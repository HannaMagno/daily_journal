from django.db import models
from django.urls import reverse
from django.utils import timezone

class JournalEntry(models.Model):
    MOOD_CHOICES = [
        ('😊', 'Happy'),
        ('😢', 'Sad'),
        ('😠', 'Angry'),
        ('😲', 'Surprised'),
        ('😴', 'Tired'),
        ('😃', 'Excited'),
        ('😌', 'Peaceful'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    mood = models.CharField(max_length=2, choices=MOOD_CHOICES, default='😊')
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Journal Entries"
        ordering = ['-date_posted']