from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from advertisement.models import Advertisement


def notify_add_comment(instance):
    adv_author = Advertisement.objects.get(id=instance.advertisement_id).author
    advertisement = instance.advertisement

    html = render_to_string(
            template_name='mail/new_comment.html',
            context={
                'comment': instance,
                'advertisement': advertisement,
            },
        )

    msg = EmailMultiAlternatives(
        subject='Новый отклик',
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to=[adv_author, ]
    )
    msg.attach_alternative(html, 'text/html')
    msg.send()


def notify_accept_comment(instance):
    comment_author = instance.author
    advertisement = instance.advertisement
    html = render_to_string(
            template_name='mail/accept_comment.html',
            context={
                'comment': instance,
                'advertisement': advertisement,
            },
        )

    msg = EmailMultiAlternatives(
        subject='Ваш отклик принят',
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to=[comment_author, ]
    )
    msg.attach_alternative(html, 'text/html')
    msg.send()