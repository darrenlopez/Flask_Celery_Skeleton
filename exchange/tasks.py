from __future__ import absolute_import
import requests
import settings
import sentry_sdk
from flask import render_template
from datetime import datetime
from exchange.celery import app
from celery.signals import celeryd_init

sentry_sdk.init(settings.SENTRY_API_KEY)

@app.task(name='tasks.health_check')
def health_check():
    try:
        sentry_sdk.capture_message('health_check: ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        response = requests.get('https://www.python.org')  
        if response.status_code:
            sentry_sdk.capture_message('health_check succeeded')
            return True
        else:
            raise Exception('Cannot Create Requests')
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return str(e)

@app.task(name='tasks.simple_request')
def simple_request():
    try:
        response = requests.get('https://www.python.org')  
        if response.status_code:
            return True
        else:
            raise Exception('Cannot Create Requests')
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return str(e)