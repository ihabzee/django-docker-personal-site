from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Section(models.Model):
    GLOBAL = 0
    PERSONAL = 1
    EXPERIANCE = 2
    EDUCATION = 3
    OTHER = 99

    class Meta:
        app_label = "resume"


    TYPES_CHOICES = (
        (GLOBAL, 'Global'),
        (PERSONAL, 'Personal'),
        (EXPERIANCE, 'Experiance'),
        (EDUCATION, 'Education'),
        (OTHER, 'Other'),
    )

    title = models.CharField(max_length=500, blank=False, null=False)

    content = HTMLField()

    type = models.PositiveBigIntegerField(choices=TYPES_CHOICES, default=0,)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField("date of creation", auto_now_add=True)

    updated_at = models.DateTimeField("date of last update", auto_now=True)