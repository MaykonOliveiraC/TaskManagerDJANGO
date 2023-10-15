from django.db import models

#descrição
#data de criação
#categoria (urgente, importante ou normal.)
#status (concluido, pendente ou adiado.)


class Tarefa(models.Model):
    OPCOES_STATUS  = (
        ('concluído', 'Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),
    )

    OPCOES_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('normal', 'Normal'),
    )


    descricao = models.CharField(max_length=400)

    criacao = models.DateTimeField(auto_now_add=True)

    categoria = models.CharField(max_length=25, choices=OPCOES_CATEGORIA, default='normal')

    status = models.CharField(max_length=25,choices=OPCOES_STATUS, default='pendente')
