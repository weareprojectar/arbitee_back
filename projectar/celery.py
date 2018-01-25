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
        'schedule': crontab(hour=23, day_of_week='sun-thu'),
        'args': ()
        },
    # 'scrape-naver-ohlvc-at-9to4': {
    #     'task': 'ohlcv-get',
    #     'schedule': crontab(minute='*/1', hour='9-16', day_of_week='mon-fri'),
    #     'args': ()
    #     },
    'get-ohlcv-01': {
        'task': 'ohlcv-get-01',
        'schedule': crontab(hour=7, day_of_week='sun-thu'),
        'args': ()
        },
    'get-ohlcv-02': {
        'task': 'ohlcv-get-02',
        'schedule': crontab(hour=7, day_of_week='sun-thu'),
        'args': ()
        },
    'get-ohlcv-03': {
        'task': 'ohlcv-get-03',
        'schedule': crontab(hour=7, day_of_week='sun-thu'),
        'args': ()
        },
    'get-ohlcv-04': {
        'task': 'ohlcv-get-4',
        'schedule': crontab(hour=7, day_of_week='sun-thu'),
        'args': ()
        },
    'get-ohlcv-05': {
        'task': 'ohlcv-get-05',
        'schedule': crontab(hour=7, day_of_week='sun-thu'),
        'args': ()
        },
    'get-ohlcv-06': {
        'task': 'ohlcv-get-06',
        'schedule': crontab(hour=7, day_of_week='sun-thu'),
        'args': ()
        },
    'get-ohlcv-07': {
        'task': 'ohlcv-get-07',
        'schedule': crontab(hour=7, day_of_week='sun-thu'),
        'args': ()
        },
    'get-ohlcv-08': {
        'task': 'ohlcv-get-08',
        'schedule': crontab(hour=7, day_of_week='sun-thu'),
        'args': ()
        },
    'get-ohlcv-09': {
        'task': 'ohlcv-get-09',
        'schedule': crontab(hour=7, day_of_week='sun-thu'),
        'args': ()
        },
    'get-ohlcv-10': {
        'task': 'ohlcv-get-10',
        'schedule': crontab(hour=7, day_of_week='sun-thu'),
        'args': ()
        },
    'get-stockinfo-01': {
        'task': 'stock-get-01',
        'schedule': crontab(minute='*/15', hour='0-7', day_of_week='mon-fri'),
        'args': ()
        },
    'get-stockinfo-02': {
        'task': 'stock-get-02',
        'schedule': crontab(minute='*/15', hour='0-7', day_of_week='mon-fri'),
        'args': ()
        },
    'get-stockinfo-03': {
        'task': 'stock-get-03',
        'schedule': crontab(minute='*/15', hour='0-7', day_of_week='mon-fri'),
        'args': ()
        },
    'get-stockinfo-04': {
        'task': 'stock-get-04',
        'schedule': crontab(minute='*/15', hour='0-7', day_of_week='mon-fri'),
        'args': ()
        },
    'get-stockinfo-05': {
        'task': 'stock-get-05',
        'schedule': crontab(minute='*/15', hour='0-7', day_of_week='mon-fri'),
        'args': ()
        },
    'get-stockinfo-06': {
        'task': 'stock-get-06',
        'schedule': crontab(minute='*/15', hour='0-7', day_of_week='mon-fri'),
        'args': ()
        },
    'get-stockinfo-07': {
        'task': 'stock-get-07',
        'schedule': crontab(minute='*/15', hour='0-7', day_of_week='mon-fri'),
        'args': ()
        },
    'get-stockinfo-08': {
        'task': 'stock-get-08',
        'schedule': crontab(minute='*/15', hour='0-7', day_of_week='mon-fri'),
        'args': ()
        },
    'get-stockinfo-09': {
        'task': 'stock-get-09',
        'schedule': crontab(minute='*/15', hour='0-7', day_of_week='mon-fri'),
        'args': ()
        },
    'get-stockinfo-10': {
        'task': 'stock-get-10',
        'schedule': crontab(minute='*/15', hour='0-7', day_of_week='mon-fri'),
        'args': ()
        },
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
