from django.db.models.signals import post_save, pre_delete
from user_coustom.models import User_custom
from django.dispatch import receiver
from .models import Candidate
@receiver(post_save, sender=User_custom)
def post_save_create_candidate(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', instance)
    print('kwargs', kwargs)
    print('created', created)
    if created:
        print(Candidate.objects.create(user=User_custom.objects.get(username = instance)))