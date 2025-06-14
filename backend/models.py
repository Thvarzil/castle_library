from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

        
class GameSystem(models.Model):
    system_name = models.CharField(max_length=200)
    is_osr = models.BooleanField(default=False)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=200)


class BookCategory(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    FORMAT_CHOICES = [
        ('PRINT', 'Print'),
        ('PDF', 'PDF'),
        ('ZINE', 'Zine'),
    ]
    
    title = models.CharField(max_length=200)
    format = models.CharField(max_length=5, choices=FORMAT_CHOICES)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    category = models.ForeignKey(BookCategory, on_delete=models.SET_NULL, null=True)
    system = models.ForeignKey(GameSystem, on_delete=models.PROTECT)
