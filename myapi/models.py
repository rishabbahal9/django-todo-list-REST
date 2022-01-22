from pydoc import describe
from django.db import models
from django.contrib import admin
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(default="", blank=True, max_length=1000)
    done = models.BooleanField(default=False)
    priority = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(3)])

    def __str__(self):
        return f"{self.title} (Priority: {self.priority}) (Done: {self.done})"


admin.site.register(Task)
