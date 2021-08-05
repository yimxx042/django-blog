from django.db import models


# Create your models here.

class Post(models.Model):
    #title #content #created Date #Modified Date
    title = models.CharField(max_length=50, unique=True, error_message={'unique': 'you already have same title!'}) #unique true, same value cant save
    content = models.TextField() #unlimied length
    db_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    db_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title