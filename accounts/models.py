from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('trainer', 'Trainer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def is_trainer(self):
        return self.role == 'trainer'

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='follows', on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

