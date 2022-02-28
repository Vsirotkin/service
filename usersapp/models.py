from django.db import models

from uuid import uuid4

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.

class User(models.Model):
    uid         = models.UUIDField(primary_key=True, default=uuid4())
    username    = models.CharField(max_length=64, unique=True)
    first_name  = models.CharField(max_length=64)
    last_name   = models.CharField(max_length=64)
    email       = models.EmailField(unique=True)
    
    def _validate_email(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False
