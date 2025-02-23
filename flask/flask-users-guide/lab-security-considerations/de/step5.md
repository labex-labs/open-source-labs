# Set-Cookie Optionen

Wenn Sie in Flask Cookies setzen, ist es wichtig, Sicherheitsoptionen zu berücksichtigen, um sensible Daten zu schützen. Einige empfohlene Optionen sind:

- Secure: Beschränkt Cookies auf HTTPS-Verkehr ausschließlich.
- HttpOnly: Schützt den Inhalt von Cookies davor, mit JavaScript gelesen zu werden.
- SameSite: Beschränkt, wie Cookies mit Anforderungen von externen Websites gesendet werden.

Beispielcode:

```python
# app.py

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('Hello, world!')
    response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
    return response

if __name__ == '__main__':
    app.run()
```

Um den Code auszuführen, speichern Sie ihn in einer Datei namens `app.py` und führen Sie den Befehl `flask run` aus.
