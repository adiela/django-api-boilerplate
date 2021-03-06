import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)
    updated_when = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
