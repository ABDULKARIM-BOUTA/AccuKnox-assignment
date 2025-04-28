# Yes signals and callers sun in the same database transaction
# so for example if the caller is rolled back the signal will be rolled back too

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class TestModel3(models.Model):
    name = models.CharField(max_length=20)

class LogMessage(models.Model):
    content = models.CharField(max_length=40)

@receiver(post_save, sender=TestModel3)
def signal_3_test(instance, sender, created, **kwargs):
    if created:
        LogMessage.objects.create(content=f'{instance.name}')

# test it in django shell:

    # python manage.py shell
    # from question_3.models import TestModel3, LogMessage
    # from django.db import transaction
    # try:
    #   with transaction.atomic():
    #       TestModel3.objects.create(name='hello')
    #       raise Exception('Force rollback')
    # except:
    #   print('rollback')

    # Output: rollback

    # you can check if a log message was created
    # print(LogMessage.objects.all())