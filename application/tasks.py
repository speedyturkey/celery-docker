from celery.schedules import crontab
from porthole import QueryExecutor, ConnectionManager
from porthole.alerts import Alert
from porthole.components import RecipientsChecker
from application.reports import samples


def get_manifest():
    return [
        {"report_name": "test_1", "schedule": crontab()},
        {"report_name": "test_2", "schedule": crontab()},
        {"report_name": "test_3", "schedule": crontab()},
    ]


def can_schedule(report):
    if not report["active"]:
        return False
    schedule_values = [
        report["schedule_minute"],
        report["schedule_hour"],
        report["schedule_day_of_week"],
        report["schedule_day_of_month"],
        report["schedule_month_of_year"]
    ]
    if any(schedule_values) and not all(schedule_values):
        send_unschedulable_alert(report)
    if all(schedule_values):
        return True
    else:
        return False


def send_unschedulable_alert(report):
    with ConnectionManager('Celery-Docker') as cm:
        checker = RecipientsChecker(cm, 'alert')
        checker.get_recipients()
    alert = Alert(
        subject=f"Unschedulable Task: {report['report_name']}",
        message="Task is active but cannot be scheduled. You must provide all cron schedule attributes, or none.",
        recipients=checker.to_recipients
    )
    alert.send()
