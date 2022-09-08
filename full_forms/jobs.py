import random
import time
from .task import *;
from apscheduler.schedulers.background import BackgroundScheduler

from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 4})
scheduler.add_jobstore(DjangoJobStore(), "default")

@register_job(scheduler, "interval",hours=2, replace_existing=True)
def test_job():
    add_full_forms_to_database()
    
register_events(scheduler)

scheduler.start()
print("Scheduler started!")

