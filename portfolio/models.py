from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    # upload_top make a file in our media files with the name projects
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Direcion Web", null=True, blank=True)
    # auto_now_add excecute one time when the intance is created
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    # auto_now it excecute every time update an intance
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
