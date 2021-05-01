from django.db import models

# Create your models here.

class EmailReachOuts(models.Model):
    first_name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=False, max_length=256)
    subject = models.CharField(blank=False, max_length=256)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.subject
