# Question Two: Yes django signals run in the sam thread as the caller
# which means when the signal is triggered, the receiver will be executed
# before the sender's code continues

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time

class TestModel2(models.Model):
    name = models.CharField(max_length=20)

@receiver(post_save, sender=TestModel2)
def test_2_signal(sender, instance, **kwargs):
    print(f'Signal Thread Id: {threading.get_ident()}')

# you can test in django shell, and you will get the same value for the caller and signal

    # python manage.py shell
    # from question_2.models import TestModel2
    # import threading
    # TestModel2.objects.create(name='Hello')
    # print(f"Caller thread ID: {threading.get_ident()}")