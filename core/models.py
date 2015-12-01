from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class Post (models.Model):
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user =  models.ForeignKey(User)

  def __unicode__(self):
    return self.description

  def get_absolute_url(self):
    return reverse("post_detail", args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __unicode__(self):
      return self.text




