from datetime import datetime

from django.core.mail import EmailMessage
from django.utils import timezone
from django.conf import settings

from translate.models import Session


def deleteOldSessions():
    # Looks up for old sessions and deletes them
    sessions = Session.objects.all()
    for session in sessions:
        if (timezone.now() - session.date_initiated).days > 0:
            session.delete()


def sendErrorLogsToMail():
    subject = "Error logs for Android String Translator"
    message = "Please find attached an email containing the error logs for Android String Translator"
    receiver = settings.EMAIL_HOST_USER
    sender = settings.EMAIL_HOST_USER  # send mail to self
    try:
        file = open("translate/errorLogs/error_log.txt", "r")
        email = EmailMessage(subject=subject, body=message, from_email=sender, to=[receiver])
        email.attach("error_log.txt", file.read(), 'text/plain')
        email.content_subtype = "text/plain"
        email.send()

    except:
        pass
