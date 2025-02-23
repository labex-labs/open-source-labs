# Implémenter la vue d'inscription

Maintenant, implémentons la vue d'inscription dans `flaskr/auth.py`. Cette vue affichera un formulaire d'inscription et traitera la soumission du formulaire.

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
            error = 'Le nom d\'utilisateur est requis.'
        elif not password:
            error = 'Le mot de passe est requis.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?,?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"L'utilisateur {username} est déjà enregistré."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```
