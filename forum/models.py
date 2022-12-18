from django.db import models

# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    when_created = models.DateTimeField(auto_now_add=True, db_index=True)




