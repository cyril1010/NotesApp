from django.db import models

class NotepadDB(models.Model):
    title = models.CharField(max_length=20,null=True,blank=True)
    note = models.CharField(max_length=200,null=True,blank=True)