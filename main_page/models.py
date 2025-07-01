from django.db import models

# Create your models here. 
class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(blank=True, null=True)
    technology = models.CharField(blank=True, null=True)
    image_url = models.URLField()
    project_link = models.URLField(blank=True, null=True)
    project_tecnology = models.ManyToManyField(Technology, blank=True)

    def __str__(self):
        return self.name