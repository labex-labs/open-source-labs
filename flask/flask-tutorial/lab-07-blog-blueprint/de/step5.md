# Beitragsaktualisierung

Wir werden den Autoren die Möglichkeit geben, ihre eigenen Beiträge zu aktualisieren. Um den Code nicht zu duplizieren, erstellen wir eine Hilfsfunktion, um einen Beitrag zu erhalten und zu überprüfen, ob der aktuelle Benutzer der Autor ist.

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
                'UPDATE post SET title =?, body =?'
                ' WHERE id =?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```
