from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from AppUser.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='posts')
    featured_image = models.ImageField(upload_to='post_images', null=True, blank=True)
    excerpt = models.CharField(max_length=200, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])

    class Meta:
        ordering = ['-created_on']

    def increment_views(self):
        self.views += 1
        self.save()

    def increment_likes(self):
        self.likes += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_related_posts(self):
        return Post.objects.filter(categories__in=self.categories.all()).exclude(id=self.id).distinct()

    def get_recent_posts(self):
        return Post.objects.filter(status='published').exclude(id=self.id).order_by('-created_on')[:5]
