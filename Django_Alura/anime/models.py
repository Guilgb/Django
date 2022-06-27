from django.db import models

# Create your models here.


class Animes(models.Model):
    idAnime = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    produtora = models.CharField(max_length=255)
    dataLancamento = models.DateTimeField()

    def __str__(self) -> str:
        return self.nomeAnime
