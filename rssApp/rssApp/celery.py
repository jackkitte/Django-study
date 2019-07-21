import feedparser
import os
import django
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rssApp.settings')

app = Celery('rssApp')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update({
    'CELERYBEAT_SCHEDULE': {
        'echo': {
            'task': 'celery_task.fetch',
            'schedule': crontab(minute='*/1')
        }
    }
})

django.setup()

from .models import Page, Feed

@app.task(name='celery_task.fetch')
def fetch():
    feeds = Feed.objects.all()
    for feed in feeds:
        try:
            rss = feedparser.parse(feed.href)
            for entry in rss.entries:
                try:
                    page_exists = Page.objects.get(href=entry.link)
                except Page.DoesNotExist:
                    page = Page.objects.create(
                        title = entry.title,
                        href = entry.link,
                        feed = feed
                    )
                    page.save()
        except Exception:
            raise