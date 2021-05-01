from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Promotion(models.Model):
    name = models.CharField(max_length=5, blank=False)
    region = models.SmallIntegerField()
    delivery = models.NullBooleanField()
    resource = models.SmallIntegerField()
    desc = models.TextField(blank=True)
    type = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return {
    #         'name': self.name, 'region': self.region, 'delivery': self.delivery, 'resource': self.resource,
    #         'desc': self.desc
    #     }

    @classmethod
    def insert(cls, name, region=0, delivery=0, resource=0, desc='', type=0,
               start_time=datetime(1900, 1, 1, 0, 0),
               end_time=datetime(1900, 1, 1, 0, 0)):
        return cls.objects.create(name=name,
                                  region=region,
                                  delivery=delivery,
                                  resource=resource,
                                  desc=desc,
                                  type=type,
                                  start_time=start_time,
                                  end_time=end_time)

    # def a(self):
    #     return self.start_time.


