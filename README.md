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

[Base de dades](https://docs.djangoproject.com/fr/2.0/intro/tutorial02/)
-------------
- Defecte: SQLite
- Connectors: https://docs.djangoproject.com/fr/2.0/topics/install/#database-installation
- Engine: https://docs.djangoproject.com/fr/2.0/ref/settings/#std:setting-DATABASE-ENGINE
- Name: os.path.join(BASE_DIR, 'db.sqlite3'),
