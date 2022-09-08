from .task import *;
from apscheduler.schedulers.background import BackgroundScheduler

from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 4})
scheduler.add_jobstore(DjangoJobStore(), "default")

@register_job(scheduler, "interval",hours=1002, replace_existing=True)
def usa_today_scrapper_job():
    usa_today_web_stories_scrapper()
    
register_events(scheduler)

scheduler.start()
print("Scheduler started!")

scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 4})
scheduler.add_jobstore(DjangoJobStore(), "default")

@register_job(scheduler, "interval",hours=1002, replace_existing=True)
def popsugr_scrapper_job():
    popsugr_web_stories_scrapper()
    
register_events(scheduler)

scheduler.start()
print("Scheduler started!")

scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 4})
scheduler.add_jobstore(DjangoJobStore(), "default")

@register_job(scheduler, "interval",hours=1002, replace_existing=True)
def best_scrapper_job():
    best_web_stories_scrapper()
    
register_events(scheduler)

scheduler.start()
print("Scheduler started!")