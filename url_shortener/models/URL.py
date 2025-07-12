from django.db import models

class URL(models.Model):
    origin_url = models.CharField()
    shortened_code = models.CharField()
    times_used = models.IntegerField(default=0)

    def _str_(self):
        return self.origin_url