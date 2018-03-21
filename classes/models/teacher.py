from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
