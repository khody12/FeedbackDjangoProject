from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.FileField(upload_to="images") # by default, this upload to will start in the very root directory of our system. not even in the root directory of the project, we must go to settings.py
    # and configure this using a new setting called MEDIA_ROOT. It will tell it where to look to store files.