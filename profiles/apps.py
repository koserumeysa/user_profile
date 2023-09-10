from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    #we have to install signals before profiles are installed.
    #thus we import it.
    #However, first the app is started, it cannot start.
    #thus we use ready method.
    def ready(self):
        import profiles.signals
