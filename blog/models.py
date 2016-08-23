from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()

    class Meta:
        ordering =['name']

    def __str__(self):
        return self.name

class Categoty(models.Model):
    category_name = models.CharField(max_length=128)
    category_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['category_name']

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=128)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name

class Article(models.Model):
    title = models.CharField(max_length=128)
    pubdate = models.DateTimeField()
    text = models.TextField()
    update = models.DateTimeField()
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Categoty)
    tags = models.ManyToManyField(Tag)
