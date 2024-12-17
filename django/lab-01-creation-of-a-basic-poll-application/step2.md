# Creating a project

If this is your first time using Django, you'll have to take care of some initial setup. Namely, you'll need to auto-generate some code that establishes a Django `project` -- a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

From the command line, `cd` into a directory where you'd like to store your code, then run the following command:

```bash
cd ~/project
django-admin startproject mysite
```

This will create a `mysite` directory in your current directory.

Let's look at what `startproject` created:

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

These files are:

- The outer `mysite/` root directory is a container for your project. Its name doesn't matter to Django; you can rename it to anything you like.
- `manage.py`: A command-line utility that lets you interact with this Django project in various ways.
- The inner `mysite/` directory is the actual Python package for your project. Its name is the Python package name you'll need to use to import anything inside it (e.g. `mysite.urls`).
- `mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
- `mysite/settings.py`: Settings/configuration for this Django project.
- `mysite/urls.py`: The URL declarations for this Django project; a "table of contents" of your Django-powered site.
- `mysite/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project.
- `mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project.
