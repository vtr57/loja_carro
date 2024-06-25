from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)

class Loja_Unidade(models.Model):
    nome = models.CharField(max_length=255)
    telefone = PhoneNumberField(unique=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    endereco_fk = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome


class Vendedor(User):
    telefone = PhoneNumberField(unique=True, null=False, blank=False)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    loja_fk = models.ForeignKey(Loja_Unidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def __str__(self) -> str:
        return super().__str__()
    
class Carro(models.Model):
    marca = models.CharField(max_length=100)
    ano = models.CharField(max_length=9)
    modelo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    km = models.IntegerField()
    cor = models.CharField(max_length=100)
    opcionais = models.TextField(max_length=500, null=True, blank=True)
    descricao = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.marca

class Cliente(User):
    data_nascimento = models.DateField()
    telefone = PhoneNumberField(unique=True, null=False, blank=False)
    avaliacao = models.TextField(max_length=500, null=True, blank=True)
    vendedor_fk = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return super().__str__()