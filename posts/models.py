from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=259)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'self.title'
    pass



