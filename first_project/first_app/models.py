from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.top_name
    
class webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class Records(models.Model):
    webpage = models.ForeignKey(webpage,on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
