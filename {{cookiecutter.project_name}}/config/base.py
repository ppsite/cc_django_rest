"""添加各环境公用配置"""
from utils.env import os, env
from config.settings import *
from config.plugins.logging import LOGGING
from config.plugins.drf import *
{%- if cookiecutter.grappelli.lower() == 'y' %}
from config.plugins.grappelli import *
{%- endif %}


# 语言/时区
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

# 允许主机
ALLOWED_HOSTS = ['*']

# 默认依赖
INSTALLED_APPS = [
    # django deps
    'django.contrib.contenttypes',
    {%- if cookiecutter.grappelli.lower() == 'y' %}
    'grappelli',
    'filebrowser',
    'grappelli.dashboard',
    {%- endif %}
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # cc_django deps
]

# 用户选项依赖
INSTALLED_APPS += [
    'rest_framework',
    {%- if cookiecutter.celery.lower() == 'y' %}
    'django_celery_beat',
    {%- endif %}
]

# 用户自定义依赖
INSTALLED_APPS += [

]

# 生产环境随机生成
SECRET_KEY = env.get('SECRET_KEY', 'NEED_TO_BE_CHANGED')

SITE_ID = 1

# 静态资源路径
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')

{%- if cookiecutter.celery.lower() == 'y' %}
# CELERY 消息队列
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL')
{%- endif %}
