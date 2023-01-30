from django.db import models

class Crawl(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title