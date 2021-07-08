from django.db import models
import uuid
# Create your models here.

class Article(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=500, null=False, blank=True)

    active = models.BooleanField(default=True)
    url = models.URLField()

    description = models.TextField(null=True, blank=True)

    image = models.ImageField(blank=True, null=True)

    image_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField("date of creation", auto_now_add=True)

    updated_at = models.DateTimeField("date of last update", auto_now=True)


    def __str__(self):
        return str(self.title)