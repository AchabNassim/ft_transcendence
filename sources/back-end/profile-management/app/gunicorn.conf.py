# Gunicorn config file
bind = "0.0.0.0:7070"
accesslog = "-"
errorlog = "-"
loglevel = "info"
timeout = 30
max_requests = 1000
workers = 5
threaded = True
