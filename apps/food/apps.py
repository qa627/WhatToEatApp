from django.apps import AppConfig


class FoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # The name must be the full Python path to the app package so Django
    # can import it correctly when INSTALLED_APPS contains 'apps.food'.
    name = 'apps.food'
