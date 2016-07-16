# Part 1: Requests and responses
> following https://docs.djangoproject.com/en/1.9/intro/tutorial01/

- create a project
 - `django-admin startproject mysite`
- `py manage.py runserver`
- ignore warning, access http://127.0.0.1:8000/ , check welcome page

> change server port: python manage.py runserver 8080
> developmnet server reload automatiocally

> project vs app : project contains app

- create app
 - `py .\manage.py startapp polls`

- Error found : TypeError: 'module' object is not iterable
 - fix: when do `from django.conf.urls import include,url`, the comma is used as "Chinese character one"

# Part 2: Models and admin sites
> https://docs.djangoproject.com/en/1.9/intro/tutorial02/

 