from django.db import models

class Blog(models.Model):
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Date = models.DateField()
    Description = models.TextField()

    def __str__(self):
        return self.Title
