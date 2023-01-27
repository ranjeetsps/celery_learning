from celery import shared_task
import time
from celery_learning.celery import app as celery_app


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(a,b):
        i=0
        while i <= 100:
            i=i+1
            time.sleep(1)
            print(i)
     

@shared_task
def xsum(numbers):
    return sum(numbers)