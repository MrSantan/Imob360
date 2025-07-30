from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'Casa'),
        ('apartment', 'Apartamento'),
        ('condo', 'Condomínio'),
        ('townhouse', 'Sobrado'),
        ('lot', 'Terreno'),
        ('commercial', 'Comercial'),
    ]
    
    TRANSACTION_TYPES = [
        ('sale', 'Venda'),
        ('rent', 'Aluguel'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Preço')
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, verbose_name='Tipo de Propriedade')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, verbose_name='Tipo de Transação')
    
    # Localização
    address = models.CharField(max_length=255, verbose_name='Endereço')
    city = models.CharField(max_length=100, verbose_name='Cidade')
    state = models.CharField(max_length=50, verbose_name='Estado')
    zip_code = models.CharField(max_length=10, verbose_name='CEP')
    
    # Características
    bedrooms = models.IntegerField(verbose_name='Quartos')
    bathrooms = models.IntegerField(verbose_name='Banheiros')
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Área (m²)')
    parking_spaces = models.IntegerField(default=0, verbose_name='Vagas de Garagem')
    
    # Imagem
    image = models.ImageField(upload_to='properties/', null=True, blank=True, verbose_name='Imagem')
    
    # Metadados
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')
    is_featured = models.BooleanField(default=False, verbose_name='Destaque')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    
    # Relacionamentos
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Proprietário')
    
    class Meta:
        verbose_name = 'Propriedade'
        verbose_name_plural = 'Propriedades'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.city}, {self.state}"
    
    def get_price_display(self):
        """Retorna o preço formatado"""
        return f"R$ {self.price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='properties/gallery/')
    caption = models.CharField(max_length=255, blank=True)
    is_main = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Imagem da Propriedade'
        verbose_name_plural = 'Imagens das Propriedades'
    
    def __str__(self):
        return f"Imagem de {self.property.title}"