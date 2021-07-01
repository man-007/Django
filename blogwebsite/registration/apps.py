from django.apps import AppConfig


class RegistrationConfig(AppConfig):
    name = 'registration'

    # for giving Signal.  
    def ready(self):
    	import registration.signal