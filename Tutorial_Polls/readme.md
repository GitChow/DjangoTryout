> the code formater: `pip install autopep8`
> another code formater: `pip install yapf` (using currently)
> the code analyzer: `pip install pylint`

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

`py .\manage.py makemigrations polls`
`py .\manage.py migrate`

> play with API, interactive shell

- `py manage.py shell` 
 - from polls.models import Question, Choice
 - Question.objects.all()
 - from django.utils import timezone
 - q = Question(question_text="What's new?", pub_date=timezone.now())
 - q.save()
 - q.id
 - q.question_text
 - q.pub_date
 - q.question_text = "what's up?"
 - q.save()
 - Question.objects.all()


- another shell test: test the newly added methods
 - from polls.models import Question, Choice
 - Question.objects.all()
 - Question.objects.filter(id=1)
 - Question.objects.filter
 - from django.utils import timezone
 - current_year = timezone.now().year
 - Question.objects.get(pub_date__year=current_year) `double underscores: field lookup`
 - Question.objects.get(pk=1)
 - q = Question.objects.get(pk=1)
 - q.was_published_recently()
 - q = Question.objects.get(pk=1)
 - q.choice_set.all()  `_set.all() query method`
 - q.choice_set.create(choice_text='Not much', votes=0)
 - q.choice_set.create(choice_text='The sky', votes=0)
 - c = q.choice_set.create(choice_text='Just hacking again', votes=0)
 - c.question
 - q.choice_set.all()
 - q.choice_set.count()
 - `Choice.objects.filter(question__pub_date__year=current_year)`
 - c = q.choice_set.filter(choice_text__startswith='Just hacking')
 - c.delete()

- create admin user
 - py manage.py createsuperuser
 - http://127.0.0.1:8000/admin/
 - make the poll app modifiable in the admin: polls/admin.py
  - from django.contrib import admin
  - from .models import Question
  - admin.site.reigster(Question)

# part3: views and templates
- paused here: I need a good one as backend of AngularJS, providing RESTFull API