from winreg import REG_OPTION_OPEN_LINK
from django.db import models
from usersapp.models import User

from uuid import uuid4

# Create your models here.

class Project(models.Model):
    uid                 = models.UUIDField(primary_key=True, default=uuid4())
    project_name        = models.CharField(max_length=64)
    repo_link           = models.LinkField(primary_key=True)
    project_user_name   = models.CharField(max_length=64)


class TODO(models.Model):
    project = models.ForeignKey('project_name', on_delete=models.CASCADE)
    todo_text = models.TextField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    todo_user = models.ForeignKey(User, on_delete=models.CASCADE)
