from django.db import models

# Create your models here.
class Animes(models.Model):
    idAnime = models.AutoField(primary_key=True)
    nomeAnime = models.CharField(max_length=255)
    descricaoAnime = models.TextField()
    dataLancamento = models.DateTimeField()
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self) -> str:
        return self.nomeAnime