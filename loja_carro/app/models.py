from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



class Endereco(models.Model):
    """
    Modelo que representa um Endereço.

    Atributos:
        rua (CharField): O nome da rua do endereço.
        cidade (CharField): A cidade do endereço.
        estado (CharField): O estado do endereço.
        numero (CharField): O número do endereço.
    """
    rua = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.rua

class Loja_Unidade(models.Model):
    """
    Modelo que representa uma Unidade de Loja.

    Atributos:
        nome (CharField): O nome da unidade da loja.
        telefone (PhoneNumberField): O número de telefone da unidade, deve ser único.
        instagram (CharField): O perfil do Instagram da unidade (opcional).
        facebook (CharField): O perfil do Facebook da unidade (opcional).
        endereco_fk (ForeignKey): Referência ao endereço da unidade.
    """
    nome = models.CharField(max_length=255)
    telefone = PhoneNumberField(unique=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    endereco_fk = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome


class Vendedor(User):
    """
    Modelo que representa um Vendedor.

    Atributos:
        telefone (PhoneNumberField): O número de telefone do vendedor, deve ser único.
        instagram (CharField): O perfil do Instagram do vendedor (opcional).
        facebook (CharField): O perfil do Facebook do vendedor (opcional).
        loja_fk (ForeignKey): Referência à unidade da loja associada ao vendedor.
    """
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
    """
    Modelo que representa um Carro.

    Atributos:
        marca (CharField): A marca do carro.
        ano (CharField): O ano de fabricação do carro.
        modelo (CharField): O modelo do carro.
        preco (DecimalField): O preço do carro.
        km (IntegerField): A quilometragem do carro.
        cor (CharField): A cor do carro.
        opcionais (TextField): Os opcionais do carro, descrição até 500 caracteres (opcional).
        descricao (TextField): Descrição adicional do carro, até 500 caracteres (opcional).
    """
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
    """
    Modelo que representa um Cliente.

    Atributos:
        data_nascimento (DateField): A data de nascimento do cliente.
        telefone (PhoneNumberField): O número de telefone do cliente, deve ser único.
        avaliacao (TextField): Uma avaliação opcional sobre o cliente, com até 500 caracteres.
        vendedor_fk (ForeignKey): Referência ao vendedor associado ao cliente.
    """
    data_nascimento = models.DateField()
    telefone = PhoneNumberField(unique=True, null=False, blank=False)
    avaliacao = models.TextField(max_length=500, null=True, blank=True)
    vendedor_fk = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return super().__str__()