from django.db import models
import uuid
import datetime

class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_id = models.PositiveIntegerField(null=True)
    author = models.CharField(max_length=255)
    descendants = models.PositiveIntegerField(null=True)
    score = models.PositiveIntegerField(null=True)
    title = models.TextField()
    type = models.CharField(max_length=255,null=True)
    url = models.URLField(max_length=1000,null=True)
    time = models.PositiveBigIntegerField(null=True)
    created_at = models.DateTimeField(null=True)

    def save(self,*args,**kwargs):
        self.created_at= datetime.datetime.fromtimestamp(float(self.time)) if self.time else datetime.datetime.now()
        super(Story, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["time"]
        verbose_name_plural = "Stories"


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_id = models.PositiveIntegerField(null=True)
    author = models.CharField(max_length=255,null=True)
    parent = models.ForeignKey(Story,on_delete=models.CASCADE,related_name="kids")
    text = models.TextField(null=True)
    time = models.PositiveBigIntegerField(null=True)
    created_at = models.DateTimeField()

    def save(self,*args,**kwargs):
        self.created_at= datetime.datetime.fromtimestamp(float(self.time)) if self.time else datetime.datetime.now()
        super(Comment, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["time"]


