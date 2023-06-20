# Python Flask Tutorial: Blueprints and Views

## Introduction

This tutorial will guide you through the process of creating and using blueprints and views in Flask. Blueprints are a way to organize a group of related views and other code. Views are the code that responds to requests made to your Flask application.

## Steps

### Step 1: Create a Blueprint

A Blueprint is a way to organize a group of related views and other code. To create a Blueprint, define a new Python module and import the necessary Flask functions and classes. Then, create an instance of the Blueprint class and define the necessary views and code within the module.

```python
# flaskr/auth.py

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
```

### Step 2: Register the Blueprint

To use the Blueprint in your Flask application, you need to register it with the application. In the factory function of your Flask application, import the Blueprint module and register it using the `app.register_blueprint()` function.

```python
# flaskr/__init__.py

def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app
```

### Step 3: Create the First View: Register

The first view we will create is the registration view. This view will handle requests to the `/auth/register` URL. It will display a form for users to fill out and handle the submission of the form.

```python
# flaskr/auth.py

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        # Validate the input
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                # Insert the new user into the database
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```

### Step 4: Create the Login View

The login view will handle requests to the `/auth/login` URL. It will display a login form and handle the submission of the form.

```python
# flaskr/auth.py

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```

### Step 5: Implement User Authentication

To implement user authentication, we need to load the logged-in user's information at the beginning of each request. We can do this by using the `before_app_request` decorator provided by Flask.

```python
# flaskr/auth.py

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
```

### Step 6: Create the Logout View

The logout view will handle requests to the `/auth/logout` URL. It will clear the user's session and redirect them to the homepage.

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```

### Step 7: Require Authentication in Other Views

To require authentication for certain views, we can create a decorator that checks if a user is logged in. If the user is not logged in, they will be redirected to the login page.

```python
# flaskr/auth.py

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```

## Summary

In this tutorial, we learned how to use blueprints and views in Flask to organize our code and handle requests. Blueprints allow us to group related views and other code together, making our application more modular and maintainable. We also implemented user authentication and created a decorator to require authentication for certain views.
