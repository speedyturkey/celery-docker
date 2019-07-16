from urllib.parse import quote_plus
from porthole import config


def get_result_backend_uri():
    default_db = config['Default']['database']
    user = config[default_db]['user']
    password = config[default_db]['password']
    host = config[default_db]['host']
    port = config[default_db]['port']
    database = config[default_db]['database']
    return f"db+postgresql://{user}:{quote_plus(password)}@{host}:{port}/{database}"


broker_url = 'redis://redis'
# Optional configuration, see the application user guide.

imports = ['application.reports.samples']
task_default_queue = 'celery-docker-queue'
task_soft_time_limit = 10 * 60
result_backend = get_result_backend_uri()
result_expires = None
result_extended = True
