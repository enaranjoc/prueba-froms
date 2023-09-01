from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    """Model definition for Task."""

    title = models.CharField( max_length=100)
    description = models.TextField('Descripción', blank=True)
    created = models.DateTimeField('Fecha de creacion', auto_now_add=True)
    datecompleted = models.DateTimeField('Fecha de finalizacion', null=True, blank=True)
    important = models.BooleanField('Importancia', default=False)
    status = models.BooleanField('Estado', default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Task."""

        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        """Unicode representation of Task."""
        return f'{self.title} - {self.user.username.capitalize()}'

