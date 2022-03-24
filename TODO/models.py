# from winreg import REG_OPTION_OPEN_LINK
from django.db import models
from usersapp.models import User

from uuid import uuid4

# Create your models here.

class Project(models.Model):
    uid                 = models.UUIDField(primary_key=True, default=uuid4())
    project_name        = models.CharField(max_length=64)
    repo_link           = models.URLField(max_length=255)
    username            = models.ManyToManyField(User)

    def __str__(self):
        return self.project_name

class TODO(models.Model):
    project         = models.ForeignKey(Project, on_delete=models.CASCADE)
    todo_text       = models.TextField(max_length=120)
    date_created    = models.DateTimeField(auto_now_add=True)
    date_updated    = models.DateTimeField(auto_now=True)
    username        = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project

    class Meta:
        ordering = ['-date_updated']