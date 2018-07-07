[Base de dades](https://docs.djangoproject.com/fr/2.0/intro/tutorial02/)
-------------
- Defecte: SQLite
- Connectors: https://docs.djangoproject.com/fr/2.0/topics/install/#database-installation
- Engine: https://docs.djangoproject.com/fr/2.0/ref/settings/#std:setting-DATABASE-ENGINE
- Name: os.path.join(BASE_DIR, 'db.sqlite3'),
- `INSTALLED_APPS`

Utilitzar la base de dades
```
$ python manage.py migrate
$ python manage.py dbshell
```

models
------
- https://docs.djangoproject.com/fr/2.0/ref/models/instances/#django.db.models.Model
- 1er, afegir al `INSTALLED_APPS = [`
- 2n, `python manage.py makemigrations <app actualitzada>`
- 3r comprovar que t'agrada el resultat
- 4t, efectuar els canvis

Veure que farà abans de fer una imigració
```
$ python manage.py sqlmigrate polls 0001
$ python manage.py check
$ python manage.py migrate # si t'agrada el resultat
```
