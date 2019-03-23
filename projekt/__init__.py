from celery import Celery

app = Celery(
    main='projekt',
    broker='redis://redis',
)
# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)
app.conf.task_default_queue = 'projekt-queue'

