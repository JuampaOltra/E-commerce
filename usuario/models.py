from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser


class Usuario(AbstractUser, PermissionsMixin):


    cif = models.CharField(
        'CIF/NIF',
        max_length= 9,
        unique=True,
        blank=True,
        null= True
    )

    is_proveedor = models.BooleanField(
        default=False,
    )


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'cif']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'








