from django.db import models
from django.conf import settings



class goal(models.Model):
    sequence_choices = [
        ('Right now', 'Right now'),
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
        ('5', 'Fifth'),
        ('6', 'Sixth'),
        ('7', 'Seventh'),
        ('8', 'Eighth'),
        ('9', 'Nineth'),
        ('10', 'Tenth'),
    ]

    executor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, blank=True, null=False, help_text="Text your goal here...")
    priority = models.CharField(choices=sequence_choices, default='Right now', max_length=10)
    status = models.CharField(default="In progress", blank=False, max_length=20)

    def get_absolute_url(self):
        return '/my-goals/'