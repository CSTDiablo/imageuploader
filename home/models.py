from django.db import models

# Create your models here.


class Image(models.Model):
    Id = models.IntegerField(primary_key=True)
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    desc = models.TextField()

    def __str__(self):
        return self.title
