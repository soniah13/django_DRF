from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date =models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title