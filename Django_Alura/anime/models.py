from django.db import models
# Esta importando a classe usuario
from django.contrib.auth.models import User


class Anime(models.Model):
    nome = models.CharField(max_length=255),
    # Nome da rota que será armazenada e acessada no banco de dados, e UNIQUE(que ele tem q ser unico)
    nome_rota = models.SlugField(max_length=255, unique=True)
    # nessa chave é onde define o tipo do usuario que registrou o anime
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # Não define o tamanho que vai ser o campo
    descricao = models.TextField()
    # Defina de forma automatica à hora da criação
    registrado = models.DateTimeField(auto_now_add=True)
    # Sempre que for modificado vai nudar
    atualizado = models.DateTimeField(auto_now=True)
