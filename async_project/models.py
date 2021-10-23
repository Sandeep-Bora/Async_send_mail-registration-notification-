from django.db import models

class Registerdb(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    register_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
