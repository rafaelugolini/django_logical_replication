import uuid

from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.db import models


# generate id for Data model
def generate_id():
    return str(uuid.uuid4())


# validate id for DataAnnotation model
def data_exist(value):
    try:
        Data.objects.get(id=value)
    except:
        return False
    return True


class Data(models.Model):
    id = models.UUIDField(
        editable=False, primary_key=True, unique=True,
        default=generate_id
    )
    data = JSONField()

    def save(self, *args, **kwargs):
        # be sure this is an append only table
        if self.id and not data_exist(self.id):
            return super().save(*args, **kwargs)
        raise ValidationError('This model is append only')


class Annotation(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, validators=[data_exist]
    )
    data = JSONField()
