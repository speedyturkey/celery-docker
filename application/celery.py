from application import app
from application import tasks


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    manifest = tasks.get_manifest()
    app.conf.beat_schedule = {
        task["report_name"]: {"task": task["report_name"], "schedule": task["schedule"]} for task in manifest
    }



