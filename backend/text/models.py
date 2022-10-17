from django.db import models
import time
# Create your models here.
from django.db import models
 
# declare a new model with a name "GeeksModel"
class TextModel(models.Model):
        # fields of the model
    query = models.CharField(max_length=500)
    time = time.time()
    response = models.CharField(max_length=500)
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.query