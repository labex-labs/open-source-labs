# Création d'un projet

Si c'est la première fois que vous utilisez Django, vous devrez prendre soin de certaines configurations initiales. Plus précisément, vous devrez générer automatiquement du code qui établit un `projet` Django - une collection de paramètres pour une instance de Django, y compris la configuration de la base de données, les options spécifiques à Django et les paramètres spécifiques à l'application.

À partir de la ligne de commande, utilisez `cd` pour accéder au répertoire où vous souhaitez stocker votre code, puis exécutez la commande suivante :

```bash
cd ~/project
django-admin startproject mysite
```

Cela créera un répertoire `mysite` dans votre répertoire actuel.

Regardons ce que `startproject` a créé :

```plaintext
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

Ces fichiers sont :

- Le répertoire racine externe `mysite/` est un conteneur pour votre projet. Son nom n'a pas d'importance pour Django ; vous pouvez le renommer comme vous le souhaitez.
- `manage.py` : Une utilité de ligne de commande qui vous permet d'interagir avec ce projet Django de diverses manières.
- Le répertoire interne `mysite/` est le véritable package Python pour votre projet. Son nom est le nom de package Python que vous devrez utiliser pour importer tout ce qui se trouve à l'intérieur (par exemple `mysite.urls`).
- `mysite/__init__.py` : Un fichier vide qui indique à Python que ce répertoire devrait être considéré comme un package Python.
- `mysite/settings.py` : Paramètres/configuration pour ce projet Django.
- `mysite/urls.py` : Les déclarations d'URL pour ce projet Django ; une "table des matières" de votre site alimenté par Django.
- `mysite/asgi.py` : Un point d'entrée pour les serveurs web compatibles ASGI pour héberger votre projet.
- `mysite/wsgi.py` : Un point d'entrée pour les serveurs web compatibles WSGI pour héberger votre projet.
