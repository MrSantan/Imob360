from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    """
    Modelo para representar os clientes de uma imobiliária.
    """

    # Informações Pessoais
    nome_completo = models.CharField(max_length=200, verbose_name="Nome Completo")
    cpf_cnpj = models.CharField(max_length=18, unique=True, blank=True, null=True, verbose_name="CPF/CNPJ")
    data_nascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")

    # Contato
    email = models.EmailField(max_length=254, unique=True, verbose_name="E-mail")
    telefone_principal = models.CharField(max_length=20, verbose_name="Telefone Principal")
    telefone_secundario = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone Secundário")

    # Endereço
    logradouro = models.CharField(max_length=255, blank=True, null=True, verbose_name="Logradouro")
    numero = models.CharField(max_length=10, blank=True, null=True, verbose_name="Número")
    complemento = models.CharField(max_length=100, blank=True, null=True, verbose_name="Complemento")
    bairro = models.CharField(max_length=100, blank=True, null=True, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade")
    estado = models.CharField(max_length=2, blank=True, null=True, verbose_name="Estado")
    cep = models.CharField(max_length=10, blank=True, null=True, verbose_name="CEP")

    # Preferências do Cliente
    TIPO_CLIENTE_CHOICES = [
        ('COMPRADOR', 'Comprador'),
        ('VENDEDOR', 'Vendedor'),
        ('LOCATARIO', 'Locatário'),
        ('LOCADOR', 'Locador'),
        ('INVESTIDOR', 'Investidor'),
        ('OUTRO', 'Outro'),
    ]
    tipo_cliente = models.CharField(
        max_length=10,
        choices=TIPO_CLIENTE_CHOICES,
        default='COMPRADOR',
        verbose_name="Tipo de Cliente"
    )
    preferencias_imovel = models.TextField(blank=True, null=True, verbose_name="Preferências do Imóvel")
    orcamento_maximo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Orçamento Máximo")

    # Metadados
    data_cadastro = models.DateTimeField(default=timezone.now, verbose_name="Data de Cadastro")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações Internas")

    class Meta:
        # Configurações adicionais do modelo
        db_table = 'clientes'  # Nome da tabela no banco de dados
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome_completo']  # Ordenação padrão por nome completo

    def __str__(self):
        # Representação legível do objeto
        return self.nome_completo