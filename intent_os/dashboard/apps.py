from django.apps import AppConfig


class DashboardConfig(AppConfig):
    default_auto_field = 'django_mongodb_backend.fields.ObjectIdAutoField'
    name = 'dashboard'

    def ready(self):
        # Clear all existing sessions on server start
        # This forces every user to log in fresh when the server restarts
        from django.contrib.sessions.models import Session
        try:
            Session.objects.all().delete()
        except Exception:
            pass  # May fail on first run if session table doesn't exist yet
