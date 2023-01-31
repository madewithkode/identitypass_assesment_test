from django.db import models

# Create your models here.

class BaseAbstractModel(models.Model):
    """
        Base Model with common fields where all
        other models can inherit from.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True

class Shortened(BaseAbstractModel):
    """
        Model representation for a shortened URLS.
    """

    original_url = models.URLField()
    shortcode = models.CharField(max_length=10)
    shortened_url = models.URLField()

    def __str__(self):
        """String representation of a shortened URL.
        """

        return 'URL - {}'.format(self.shortened_url)
