from django.db import models

# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    #owner_comment = models.TextField() # this is something that should not be exposed to end user

