# Creating the Polls app

Now that your environment -- a "project" -- is set up, you're set to start doing work.

Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

> Projects vs. apps
> What's the difference between a project and an app? An app is a web application that does something -- e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

Your apps can live anywhere on your `Python path <tut-searchpath>`. In this tutorial, we'll create our poll app in the same directory as your `manage.py` file so that it can be imported as its own top-level module, rather than a submodule of `mysite`.

To create your app, make sure you're in the same directory as `manage.py` and type this command:

```bash
cd ~/project/mysite
python manage.py startapp polls
```

That'll create a directory `polls`, which is laid out like this:

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

This directory structure will house the poll application.
