# Führen Sie die Anwendung mit einem Produktionsserver aus

Für eine Produktionsumgebung sollten Sie einen WSGI-Server statt des eingebauten Entwicklungsservers verwenden. Wir werden Waitress als unseren WSGI-Server verwenden.

Zunächst installieren Sie Waitress:

```bash
# Installieren Sie Waitress
pip install waitress
```

Nun sagen Sie Waitress, Ihre Anwendung zu servieren:

```bash
# Führen Sie die Anwendung mit Waitress aus
waitress-serve --call 'flaskr:create_app'
```
