import os

USERNAME = os.environ.get('USERNAME', '')
PASSWORD = os.environ.get('PASSWORD', '')
DATA_DIR = os.environ.get('DATA_DIR', '')
JOBS_TO_KEEP = os.environ.get('JOBS_TO_KEEP', 5)
MAX_PROC = os.environ.get('MAX_PROC', 0)
MAX_PROC_PER_CPU = os.environ.get('MAX_PROC_PER_CPU', 4)
FINISHED_TO_KEEP = os.environ.get('FINISHED_TO_KEEP', 100)
POLL_INTERVAL = os.environ.get('POLL_INTERVAL', 5.0)
BIND_ADDRESS = os.environ.get('BIND_ADDRESS', '0.0.0.0')
HTTP_PORT = os.environ.get('HTTP_PORT', 6800)
DEBUG = os.environ.get('DEBUG', 'off')

conf = f"""
[scrapyd]
username         = {USERNAME}
password         = {PASSWORD}
eggs_dir         = {DATA_DIR}/eggs
logs_dir         = {DATA_DIR}/logs
items_dir        = {DATA_DIR}/items
dbs_dir          = {DATA_DIR}/dbs
jobs_to_keep     = {JOBS_TO_KEEP}
max_proc         = {MAX_PROC}
max_proc_per_cpu = {MAX_PROC_PER_CPU}
finished_to_keep = {FINISHED_TO_KEEP}
poll_interval    = {POLL_INTERVAL}
bind_address     = {BIND_ADDRESS}
http_port        = {HTTP_PORT}
debug            = {DEBUG}
runner           = scrapyd.runner
application      = scrapyd.app.application
launcher         = scrapyd.launcher.Launcher
webroot          = scrapyd.website.Root

[services]
schedule.json     = scrapyd.webservice.Schedule
cancel.json       = scrapyd.webservice.Cancel
addversion.json   = scrapyd.webservice.AddVersion
listprojects.json = scrapyd.webservice.ListProjects
listversions.json = scrapyd.webservice.ListVersions
listspiders.json  = scrapyd.webservice.ListSpiders
delproject.json   = scrapyd.webservice.DeleteProject
delversion.json   = scrapyd.webservice.DeleteVersion
listjobs.json     = scrapyd.webservice.ListJobs
daemonstatus.json = scrapyd.webservice.DaemonStatus
"""

print(conf)
