# Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) ist ein Angriff, bei dem Benutzer dazu gebracht werden, unbeabsichtigte Aktionen auf einer Website auszuführen. Um CSRF-Angriffe in Flask zu verhindern, folgen Sie diesen Richtlinien:

- Verwenden Sie einmalige Token, um Anforderungen zu validieren, die den Serverinhalt ändern.
- Speichern Sie das Token im Cookie und übermitteln Sie es mit den Formulardaten.
- Vergleichen Sie das empfangene Token auf dem Server mit dem im Cookie gespeicherten Token.

Beispielcode:

```python
# app.py

from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        token = request.form.get('token')
        if token and token == session.get('csrf_token'):
            # Delete user profile
            return redirect(url_for('index'))
    return 'Invalid request'

if __name__ == '__main__':
    app.run()
```

Um den Code auszuführen, speichern Sie ihn in einer Datei namens `app.py` und führen Sie den Befehl `flask run` aus.
