from celery import shared_task
import time


@shared_task
def add(x, y):
    i=0
    while i <= 100:
        i=i+1
        time.sleep(1)
        print(i,"add")
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