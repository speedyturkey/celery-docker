from celery import Celery, Task
from porthole.alerts import Alert
from application import celeryconfig

app = Celery(
    main='celery-docker'
)
app.config_from_object(celeryconfig)


class CustomTask(Task):

    def on_failure(self, exception, task_id, args, kwargs, traceback):
        alert = Alert(
            subject=f"{self.app.main} task failure: {self.name}",
            message=f"""Project: {self.app.main}
Task:       {self.name}
Args:       {args}
Kwargs:     {kwargs}
Exception:  {exception}
Task ID:    {task_id}

Traceback: {traceback}
"""
        )
        alert.send()
