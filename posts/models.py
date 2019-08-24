from tinymce import HTMLField

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Language(models.Model):
    LANGUAGE_CHOICES = (('EN','Anglès'),
                        ('ES','Espanyol'),
                        ('CA','Català'))
    llenguatge = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='CA')

    def __str__(self):
        return self.llenguatge

    class Meta:
        verbose_name_plural = 'Llenguatges'


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = HTMLField('Content') # Texte central
    overview = models.TextField() # Texto en el separador
    title_last_posts = models.CharField(max_length=100,default="Title")
    description_last_posts = models.TextField(default="last posts")
    title_newsletter = models.CharField(max_length=100, default="title")
    description_news_letter=models.TextField(default="Newsletter text")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    content = HTMLField('Content')
    comments_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnal = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey("self", related_name="previous", on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey("self", related_name="next", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("post-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("post-delete", kwargs={"id": self.id})

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
