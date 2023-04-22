from django.db import models
import datetime

#tabela de produtos
class Produto(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome
    
#tabela de vendedor
class Vendedor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


#tabela de vendas
class Vendas(models.Model):
    produto  = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    total    = models.FloatField()
    data     = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self) -> str:
        return 'Produto => '+ self.produto.nome + " || Vendedor => " + self.vendedor.nome