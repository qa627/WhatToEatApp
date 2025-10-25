from .base import *

DEBUG = False
ALLOWED_HOSTS = ['www.yourdomain.com']

# 生產環境安全設定
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
