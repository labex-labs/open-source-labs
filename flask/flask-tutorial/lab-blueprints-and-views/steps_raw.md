# Flask Blueprint Lab

## Introduction

In this lab, we will walk through how to create and use Flask blueprints to structure your application using views. Flask blueprints allow you to group related views, code, and resources together making your application modular and scalable. We will create a simple application which will include user authentication and blog posts functionality.

## Steps

### Step 1: Create a Blueprint

Let's start by creating a blueprint for our application. This blueprint will be named 'auth' and will handle user authentication related views. We will define our blueprint in a separate module named `flaskr/auth.py`.

```python
# flaskr/auth.py

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

# Create a Blueprint named 'auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')
```

### Step 2: Register the Blueprint

After creating the blueprint, we need to register it with our application. This is done in the application factory function in `flaskr/__init__.py`.

```python
# flaskr/__init__.py

def create_app():
    app = ...
    # existing code omitted

    # Import and register the blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    return app
```

### Step 3: Implement Registration View

Now, let's implement the registration view in `flaskr/auth.py`. This view will render a registration form and handle form submission.

```python
# flaskr/auth.py

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
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

### Step 4: Implement Login View

Next, we will implement the login view in `flaskr/auth.py`. This view will handle user login functionality.

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

### Step 5: Implement Logout View

Let's now add a logout view in `flaskr/auth.py`. This view will handle user logout functionality.

```python
# flaskr/auth.py

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```

### Step 6: Implement Login Required Decorator

We will also need a decorator to protect our views that require a user to be logged in. This decorator will be implemented in `flaskr/auth.py`.

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

In this lab, we have learned how to use Flask blueprints to structure our application. We have created a blueprint for user authentication and implemented registration, login, and logout views. We also implemented a decorator to protect views that require a user to be logged in. With this knowledge, you can now structure your Flask applications in a modular and scalable manner.
