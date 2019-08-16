# Happy Logger

A tool to log data http-posted from a device to database, view and filter the messages, export
to database. Can use sqlite or mysql, yet adding any django-compatible database should be trivial.

Example query to create the message
```
 curl -d "Message text" -H 'X-Logger-Hostname: Whatever' -H 'X-Logger-Token: secret' -X POST http://happylogger
```

Accepted HTTP headers

* `X-Logger-Hostname` - hostname, that is saved to database. If not provided, IP address is used
* `X-Logger-Token` - security token, to prevent unauthorized messages. Defaults to secret. Can be set in 
  environment with `LOGGER_SECURITY_TOKEN` variable.

## Configuration

To configure, set environment variables

* `LOGGER_SECURITY_TOKEN` - security token value
* `MYSQL_HOST` - mysql database host, if not set sqlite is used
* `MYSQL_PORT` - mysql database port, default is 3306
* `MYSQL_DB` - mysql database port, default is happy_log
* `MYSQL_USER` - mysql database port, default is happy_log
* `MYSQL_PASSWORD` - mysql database port, default is happy_log

## Initial setup

Set environment variables mentioned above

Create first admin user with
```
python manage.py createsuperuser
```

Do setup applicable for your web server to run wsgi application, located in `logger/logger/wsgi.py`