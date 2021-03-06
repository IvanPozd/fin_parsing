from celery import Celery
from celery.schedules import crontab
from master import master


CELERY_TIMEZONE = 'Europe/Moscow'


celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def main():
    master()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=15, minute=0, day_of_week="mon-fri"), main.s())