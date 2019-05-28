from __future__ import absolute_import
from celery import Celery
import os
broker_url = os.environ.get('CELERY_BROKER_URL') or 'amqp://user:pass@rabbit:5672//'
result_backend = os.environ.get('CELERY_RESULT_BACKEND') or 'rpc://'
app = Celery('exchange', broker=broker_url,backend=result_backend)
default_config = 'exchange.celeryconfig'
app.config_from_object(default_config)
