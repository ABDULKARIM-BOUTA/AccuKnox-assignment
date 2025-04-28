# Question One: By default django signals are executed synchronously
# Which means all the receivers associated with the signal are executed immediately
# and each one must complete before the next one starts

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time

class TestModel(models.Model):
    name = models.CharField(max_length=20)

@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, **kwargs):
    print('Start')
    time.sleep(10)
    print('End')

# you can test in django shell:

    # python manage.py shell
    # from question_1.models import TestModel
    # TestModel.objects.create(name='Hello')

#--------------------------------------------
