from django.db import models

# Create your models here.


class question(models.Model):
    pass


class choice(models.Model):
    question_name = models.CharField(max_length=255)
    pass


class score(models.Model):
    pass
