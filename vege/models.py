from django.db import models

# Create your models here.
# class Recepie(models.Model):
#     recepie_name = models.CharField(max_length=100)
#     recepie_description = models.TextField()
#     recepie_image = models.ImageField(upload_to="recepie")




from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title
