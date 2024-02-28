from django.db import models

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    fecha_publi = models.DateField(("DD/MM/AA"),null=True, auto_now=False, auto_now_add=False)
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return self.title