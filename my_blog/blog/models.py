from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length =120)
    last_name = models.CharField(max_length =120)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Rating(models.Model):
    caption = models.CharField(max_length=10)
    def __str__(self):
        return self.caption



class Article(models.Model):
    title = models.CharField(max_length=180)
    brief_read = models.CharField(max_length=350)
    image_name =models.ImageField(upload_to="images")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField( validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    rating = models.ManyToManyField(Rating)

class Thoughts(models.Model):
    user = models.CharField(max_length=150)
    email = models.EmailField()
    text = models.TextField(max_length=400)
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="thoughts")

    #add date when post was created






