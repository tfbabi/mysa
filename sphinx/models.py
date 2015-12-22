from django.db import models

# Create your models here.

class Sphinxinfo(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    sshport = models.CharField(max_length=100)
    indexerbin = models.CharField(max_length=200)
    conf = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class sshinfo(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
