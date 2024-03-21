from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models


class Templates(models.Model):
    HTML_page = models.TextField()
    user = models.ForeignKey(User,on_delete=models.PROTECT)


