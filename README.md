# celery
Learning celery and celery beat



INSTALL the django-celery first then go through the steps:
Step 1 :
pip install django-celery

Step 2 : 
In the project folder where the settings.py file exists, create a new Python file named celery.py.

((The above configuration creates a Celery application using the Django settings. app.autodiscover_tasks() tries to discover a file named task.py in all of our Django applications.))

Step 3 :
In the __init__.py file within the package where settings.py file is located, add the code snippet below
[from .celery import app as celery_app

__all__ = ['celery_app']]

The above code snippet imports Celery every time our application starts.

Step 4 : register your created  app (app) in your settings.py


Step 5 : Install the django-celery-results library:
pip install django-celery-results

((The django-celery-results extension provides result backends using either the Django ORM, or the Django Cache framework.))

Step 6 :
Add django_celery_results to INSTALLED_APPS in your Django project’s settings.py:

INSTALLED_APPS = (
    ...,
    'django_celery_results',
)

Step 7 :
Create the Celery database tables by performing a database migrations:

python manage.py migrate django_celery_results

Step 8 :
Start worker process

celery -A proj worker -l INFO

