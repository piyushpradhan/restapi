from django.db import models

class TitleModel(models.Model):
    title = models.CharField(max_length=100)

    def _str_(self):
        return self.title

class DescModel(models.Model):
    desc = models.CharField(max_length=500)

    def _str_(self):
        return self.desc