from django.contrib import admin

from .models import Carro, Cliente, Loja_Unidade, Endereco, Vendedor

class CarroAdmin(admin.ModelAdmin):
    list_display = ['marca', 'ano', 'modelo', 'km']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['username']

class Loja_UnidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['rua']

class VendedorAdmin(admin.ModelAdmin):
    list_display = ['username','email']

admin.site.register(Carro, CarroAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Loja_Unidade, Loja_UnidadeAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Vendedor, VendedorAdmin)