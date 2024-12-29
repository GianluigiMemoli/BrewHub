from django.db import models
from django.db.models import Model
from django.db.models.fields import DateTimeField
from django.utils import timezone
import nanoid


def generate():
    return nanoid.generate(
        alphabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        size=15,
    )


# Create your models here.
class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    id = models.CharField(
        max_length=21, primary_key=True, default=generate, editable=False
    )

    def save(self, *args, **kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
