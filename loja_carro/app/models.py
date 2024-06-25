from django.db import models
from django.contrib.auth.models import User


class Vendedor(User):
    telefone = models.