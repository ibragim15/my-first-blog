from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class MyProject(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    text = models.TextField()
    address = models.CharField(max_length=79)
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
