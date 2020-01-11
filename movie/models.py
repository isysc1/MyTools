from django.db import models


class Information(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    reviews = models.CharField(max_length=255, null=False)
    time = models.DateField(null=False)
    image_Url1 = models.CharField(max_length=2550, null=False)
    image_Url2 = models.CharField(max_length=2550, null=False)
    kind = models.CharField(max_length=255, null=False)
    score = models.CharField(max_length=255, null=False)


class totalModel(models.Model):
    viewingTimes = models.CharField(max_length=255, null=False)