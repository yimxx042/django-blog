from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols

# Create your models here.

class Post(models.Model):
    #title #content #created Date #Modified Date
    title = models.CharField(max_length=50, unique=True, error_messages={'unique': 'you can`t use the same title!'}) #unique true, same value cant save
    content = models.TextField(validators=[MinLengthValidator(10, 'too short, add more than 10.'), validate_symbols]) #add mord then 10 
    db_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    db_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title