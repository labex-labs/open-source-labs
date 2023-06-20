# Flask Blog Blueprint

## Introduction

In this lab, you will learn how to implement a blog blueprint using Flask. The blog blueprint will allow users to create, edit, and delete blog posts. We will cover the following steps:

1. Define and register the blueprint
2. Implement the index view to display all posts
3. Implement the create view to allow users to create new posts
4. Implement the update view to allow users to edit existing posts
5. Implement the delete view to allow users to delete posts

## Steps

### Step 1: Define and register the blueprint

Create a new file called `blog.py` and add the following code:

```python
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
```

### Step 2: Implement the index view

In the `blog.py` file, add the following code to implement the index view:

```python
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

### Step 3: Implement the create view

In the `blog.py` file, add the following code to implement the create view:

```python
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

### Step 4: Implement the update view

In the `blog.py` file, add the following code to implement the update view:

```python
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


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

### Step 5: Implement the delete view

In the `blog.py` file, add the following code to implement the delete view:

```python
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

Congratulations! You have successfully implemented a blog blueprint using Flask. The blog blueprint allows users to create, edit, and delete blog posts. You have learned how to define and register a blueprint, implement views for listing, creating, updating, and deleting posts, and use templates to render the views. Keep practicing and exploring Flask to build more powerful web applications.
