from datetime import datetime
from django.utils import timezone

from translate.models import Session


def deleteOldSessions():
    # Looks up for old sessions and deletes them
    sessions = Session.objects.all()
    for session in sessions:
        if (timezone.now() - session.date_initiated).days > 0:
            session.delete()

