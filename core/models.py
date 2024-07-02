from django.contrib.auth.models import User
from django.db import models

from roles.models import Role
from status.models import Status


# Create your models here.
class DetailUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    role = models.ForeignKey(Role, on_delete=models.CASCADE,)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, )
    observacao = models.TextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
