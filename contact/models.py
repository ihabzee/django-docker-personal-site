from django.db import models
import uuid
# Create your models here.

class Contact(models.Model):
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    subject = models.CharField(max_length=500)

    content = models.TextField()

    email = models.EmailField()

    created_at = models.DateTimeField("date of creation", auto_now_add=True)

    updated_at = models.DateTimeField("date of last update", auto_now=True)