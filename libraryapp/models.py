from django.db import models

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    published_year = models.IntegerField()
    copies_available = models.IntegerField()

    def __str__(self):
        return self.title

class Borrower(models.Model):
    borrower_id = models.AutoField(primary_key=True)
    borrower_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.borrower_name
