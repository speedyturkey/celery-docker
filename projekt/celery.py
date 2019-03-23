from projekt import app
from celery.schedules import crontab


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s('hello world'), options={'queue': 'projekt-queue'})


@app.task
def test(arg):
    print(arg)
