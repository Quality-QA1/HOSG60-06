from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth.hashers import make_password

class UsuarioManager(BaseException):
    def create_user(self,username,password=None):
        if not username:
            raise ValueError('Los Usuarios Deben Tener Un Usuario Asignado')
        user=self.model(username=username)
        user.self_password(password)
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(primary_key=True,max_length=20,unique=True)
    password=models.CharField('Password',max_length=100)
    perfil=models.CharField('Perfil',max_length=35)
    nombre=models.CharField('Nombre',max_length=30)
    apellidos=models.CharField('Apellidos',max_length=30)
    telefono=models.CharField('Telefono',max_length=20)
    genero=models.CharField('Genero',max_length=15)

    def save(self, **kwargs):
        some_salt='mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UsuarioManager()
    USERNAME_FIELD = 'username'



