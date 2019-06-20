from django.db import models
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    """Model definition for Post."""

    # TODO: Define fields here
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    
    body = models.TextField()

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args = [str( self.id )])
