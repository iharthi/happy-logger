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
* `DJANGO_ALLOWED_HOSTS` - set this to comma-separated list of hostnames to run on, like `domain1.com,domain2.com`
* `DJANGO_SECURITY_KEY` - Django security key, set this to random string in production. See https://docs.djangoproject.com/en/dev/ref/settings/#secret-key

## Initial setup

Set environment variables mentioned above

Apply migrations to create database tables
```
python manage.py migrate
```

Compile translation messages, to enable localized interface
```
python manage.py compilemessages
```

Collect static files to be served by the web server
```
python manage.py collectstatic
```

Create first admin user with
```
python manage.py createsuperuser
```

Do setup applicable for your web server to run wsgi application, located in `logger/logger/wsgi.py`

Configure your web server so that `static` directory is available under `/static/`.