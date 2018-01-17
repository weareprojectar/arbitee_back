from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectar.settings')

app = Celery('proj')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

from celery.schedules import crontab
app.conf.beat_schedule = {
    'add-every-60-seconds': {
        'task': 'scrape_upbit',
        'schedule': 60.0,
        'args': ()
        },
    'add-every-0.5-seconds': {
        'task': 'scrape_upbit_price',
        'schedule': 0.5,
        'args': ()
        },
    }
