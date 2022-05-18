web: uwsgi --ini /workspace/uwsgi.ini
{%- if cookiecutter.celery.lower() == 'y' %}
beat: celery -A {{cookiecutter.project_name}} beat -l info
worker: celery -A {{cookiecutter.project_name}} worker -l INFO
{%- endif %}