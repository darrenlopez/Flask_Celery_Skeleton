from datetime import timedelta

CELERY_IMPORTS = ("exchange.tasks", )


CELERYBEAT_SCHEDULE = {
    'health-check': {
        'task': 'tasks.health_check',
        'schedule': timedelta(minutes=1)
    }
}
