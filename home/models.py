from django.db import models


class Group(models.Model):
    g_name=models.CharField(max_length=50)
    def __str__(self):
        return self.g_name

class chat(models.Model):
    content=models.CharField(max_length=200)
    time=models.DateTimeField(auto_now=True)
    group=models.ForeignKey(Group,on_delete=models.CASCADE)    

    def __str__(self):
        return self.content

# Create your models here.
