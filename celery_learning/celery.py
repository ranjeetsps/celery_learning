import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_learning.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

from kombu import Exchange, Queue



CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"


# routing and queue configuration
app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'default'
app.conf.task_default_routing_key = 'default'

default_exchange = Exchange('default', type='direct')
mul_exchange = Exchange('multiply', type='direct')
add_exchange = Exchange('add', type='direct')


app.conf.task_queues = (
    Queue('default', default_exchange, routing_key='default'),
    Queue('multiply', mul_exchange, routing_key='multiply'),
    Queue('add', add_exchange, routing_key='add')
)

app.conf.task_routes = ([{
    'api.tasks.mul': {'queue': 'multiply', 'priority': 10},
},
{
    'api.tasks.add': {'queue': 'add', 'priority': 0},
},
])