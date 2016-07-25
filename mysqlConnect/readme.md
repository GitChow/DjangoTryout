> ImportError: No module named 'MySQLdb'. Error in Windows.

Fix: install and use pymysql
in settings.py
```
import pymysql
pymysql.install_as_MySQLdb()
```


> Table 'xxxx.auth_user' doesn't exist" after login 127.0.0.1/admin
Fix: get a clean database
- manage.py syncdb
- manage.py migrate
- create super user
  - py manage.py createsuperuser
