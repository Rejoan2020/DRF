from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 50)
    Students_Id   = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name