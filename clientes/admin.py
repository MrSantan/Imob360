from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'telefone_principal', 'tipo_cliente', 'data_cadastro')
    search_fields = ('nome_completo', 'email', 'cpf_cnpj', 'telefone_principal')
    list_filter = ('tipo_cliente', 'data_cadastro', 'cidade')
    date_hierarchy = 'data_cadastro'