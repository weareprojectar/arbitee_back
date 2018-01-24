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
    # 'add-every-60-seconds': {
    #     'task': 'scrape_upbit',
    #     'schedule': 60.0,
    #     'args': ()
    #     },
    'scrape-daum-ticker-at-9': {
        'task': 'stock-ticker',
        'schedule': crontab(hour=8, day_of_week='mon-fri'),
        'args': ()
        },
    # 'scrape-naver-ohlvc-at-9to4': {
    #     'task': 'ohlcv-get',
    #     'schedule': crontab(minute='*/1', hour='9-16', day_of_week='mon-fri'),
    #     'args': ()
    #     },
    'get-ohlcv-1': {
        'task': 'ohlcv-get-1',
        'schedule': 20.0,
        'args': ()
        },
    # 'get-ohlcv-2': {
    #     'task': 'ohlcv-get-2',
    #     'schedule': 20.0,
    #     'args': ()
    #     },
    # 'get-ohlcv-3': {
    #     'task': 'ohlcv-get-3',
    #     'schedule': 20.0,
    #     'args': ()
    #     },
    # 'get-ohlcv-4': {
    #     'task': 'ohlcv-get-4',
    #     'schedule': 20.0,
    #     'args': ()
    #     },
    # 'get-ohlcv-5': {
    #     'task': 'ohlcv-get-5',
    #     'schedule': 20.0,
    #     'args': ()
    #     },
    'get-stockinfo-1': {
        'task': 'stock-get-1',
        'schedule': 20.0,
        'args': ()
        },
    # 'get-stockinfo-2': {
    #     'task': 'stock-get-2',
    #     'schedule': 20.0,
    #     'args': ()
    #     },
    # 'get-stockinfo-3': {
    #     'task': 'stock-get-3',
    #     'schedule': 20.0,
    #     'args': ()
    #     },
    # 'get-stockinfo-4': {
    #     'task': 'stock-get-4',
    #     'schedule': 20.0,
    #     'args': ()
    #     },
    # 'get-stockinfo-5': {
    #     'task': 'stock-get-5',
    #     'schedule': 20.0,
    #     'args': ()
    #     },
    }
app.conf.timezone = 'Asia/Seoul'


# 'add-every-0.5-seconds': {
#     'task': 'scrape_upbit_price',
#     'schedule': 0.5,
#     'args': ()
#     },
# 'add-every-1-minutes': {
#     'task': 'kospi-ticker',
#     'schedule': 60.0,
#     'args': ()
#     },
# 'add-every-1-minutes': {
#     'task': 'kosdaq-ticker',
#     'schedule': 60.0,
#     'args': ()
#     },
