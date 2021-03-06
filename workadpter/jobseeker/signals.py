from django.db.models.signals import post_save, pre_delete
from user_coustom.models import User_custom
from django.dispatch import receiver
from .models import Candidate
@receiver(post_save, sender=User_custom)
def post_save_create_employer(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', instance)
    print('kwargs', kwargs)
    print('created', created)
    if created:
        u = sender.objects.get(username=instance)
        if u.iscandidate==True:
            e = Candidate(user=u)
            e.save()