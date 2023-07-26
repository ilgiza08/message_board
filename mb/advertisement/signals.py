from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import notify_add_comment, notify_accept_comment
from .models import Comment
 
 
@receiver(post_save, sender=Comment)
def notify_authors(sender, instance, created, **kwargs):
    if created:
        notify_add_comment(instance)
    else:
        notify_accept_comment(instance)