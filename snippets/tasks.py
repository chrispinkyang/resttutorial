from tutorial import celery_app
from time import sleep
from .models import Snippet

@celery_app.task
def add(x,y):
	sleep(2)
	return x+y


@celery_app.task
def async_test():
	another = Snippet.objects.get(pk=2)
	return another.code