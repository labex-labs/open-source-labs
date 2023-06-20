# Flask Blog Application Lab

## Introduction

In this lab, we'll walk through creating a blog application using Flask, a popular web framework in Python. This application will list all blog posts, allow logged-in users to create posts, and let authors edit or delete their own posts.

## Steps

### Step 1: Define Blueprint

Firstly, we'll define a blueprint for our blog. A blueprint is a way to organize a group of related views and other code.

```python
# flaskr/blog.py

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

# The Blueprint is named 'blog'. It's defined in the same file.
# The blueprint needs to know where it's defined, so __name__ is passed as the second argument.
bp = Blueprint('blog', __name__)
```

### Step 2: Register Blueprint

Next, we'll register the blueprint with our application.

```python
# flaskr/__init__.py

def create_app():
    app = ...
    # existing code omitted

    # import and register the blueprint from the factory using app.register_blueprint()
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```

### Step 3: Create Blog Index

Now, let's create an index view to display all blog posts. We'll use a SQL `JOIN` to include author information from the `user` table in our results.

```python
# flaskr/blog.py

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
```

### Step 4: Post Creation

Next, we'll create a view that allows logged-in users to create new blog posts.

```python
# flaskr/blog.py

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
```

### Step 5: Post Update

We'll add the ability for authors to update their own posts. To avoid duplicating code, we'll create a helper function to get a post and check if the current user is the author.

```python
# flaskr/blog.py

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```

### Step 6: Post Deletion

Lastly, we'll add the ability for authors to delete their own posts.

```python
# flaskr/blog.py

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
```

## Summary

Congratulations, you've created a simple blog application using Flask! This application supports user authentication, and allows users to create, edit, and delete their own blog posts.
