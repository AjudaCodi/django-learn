Django
======

Tota la informació en frances
- https://docs.djangoproject.com/fr/2.0/

Tutorial
- https://docs.djangoproject.com/fr/2.0/intro/tutorial01/

Pas per pas
===========
Comprovar que està instaŀlat
```
$ python -m django --version
```
Creació d'un projecte
```
$ django-admin startproject mysite
```
- __manage.py__ línia de [comandes](https://docs.djangoproject.com/fr/2.0/ref/django-admin/)
- __mysite/__
  - __\_\_init\_\_.py__ Fitxer buit per indicar que és un [packet](https://docs.python.org/3/tutorial/modules.html#tut-packages)
  - __settings.py__ [Configuració](https://docs.djangoproject.com/fr/2.0/topics/settings/)
  - __urls.py__ [Distribució](https://docs.djangoproject.com/fr/2.0/topics/http/urls/)
  - __wsgi.py__ [Servidors](https://docs.djangoproject.com/fr/2.0/howto/deployment/wsgi/)

Arrancar django
```
$ python manage.py runserver
```

Creació d'una applicació
```
$ python manage.py startapp polls
```

- [Bases de dades](READMES/BD.md)

Shell
-----
```
$ python manage.py shell
>>> from polls.models import Choice, Question
>>> Question.objects.all()

>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()

# Show information
>>> q.id
>>> q.question_text
>>> q.pub_date

# edit
>>> q.question_text = "What's up?"
>>> q.save()
```

Més sobre la shell
------------------
```
>>> Question.objects.filter(id=1)
>>> Question.objects.get(pk=1)
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
```

Administrador
-------------
```
$ python manage.py createsuperuser
```

- https://docs.djangoproject.com/fr/2.0/intro/tutorial03/

- [Vistes](READMES/vistes.md)
