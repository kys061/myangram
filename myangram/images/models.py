from django.db import models
from myangram.users import models as user_models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Image(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, related_name='images')

    @property
    def like_count(self):
        return self.likes.all().count()     # likes is the related name in model class Like

    def __str__(self):
        return 'loc: {}, cap: {}'.format(self.location, self.caption)

    class Meta:
        ordering = ['-created_at']


@python_2_unicode_compatible
class Comment(TimeStampedModel):

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True)
    image = models.ForeignKey(Image, null=True, related_name='comments')

    def __str__(self):
        return 'who: {} - msg: {} at {}'.format(self.creator, self.message, self.created_at)


@python_2_unicode_compatible
class Like(TimeStampedModel):

    creator = models.ForeignKey(user_models.User, null=True)
    image = models.ForeignKey(Image, null=True, related_name='likes')

    def __str__(self):
        return 'who: {} - msg: {} at {}'.format(self.creator, self.image, self.created_at)
