from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Tag(models.Model):
    lable = models.CharField(max_length=255)




class TaggedItem(models.Model):
    #what tag is applied to what object

    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE)
    # type (product)
    # id (product id)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey


