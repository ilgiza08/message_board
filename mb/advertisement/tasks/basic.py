from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from advertisement.models import Advertisement
from django.contrib.auth.models import User
import datetime


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


def notify_weekly():
    email_list = list(User.objects.values_list("email", flat=True))
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=7)
    advertisements = Advertisement.objects.filter(created__range=(start_date, end_date))

    html = render_to_string(
        template_name='mail/weekly_mailing.html',
        context={
            'advertisements': advertisements,
        },
    )
    
    msg = EmailMultiAlternatives(
        subject='Новые обявления',
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to=[email_list, ],
    )
    msg.attach_alternative(html, 'text/html')
    msg.send()