from django.db import migrations, models

# Create your models here.


class Category(models.Model):

    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Author(models.Model):

    author_name = models.CharField(max_length=100)


    def __str__(self):
        return self.author_name






class Book(models.Model):
    day = models.DateField()
    book_name = models.CharField(max_length=100)
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_author = models.CharField(max_length=100)
    book_context = models.CharField(max_length=1000)

    def __str__(self):
        return self.book_name
