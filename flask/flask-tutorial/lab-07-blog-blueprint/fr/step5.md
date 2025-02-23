# Mise à jour d'un article

Nous allons ajouter la possibilité pour les auteurs de modifier leurs propres articles. Pour éviter de dupliquer le code, nous allons créer une fonction d'aide pour obtenir un article et vérifier si l'utilisateur actuel est l'auteur.

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
            error = 'Le titre est requis.'

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
