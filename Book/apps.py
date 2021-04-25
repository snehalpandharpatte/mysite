from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Book'




def my_gen():
    yield 1
    yield 2
    yield 3
    yield 4

