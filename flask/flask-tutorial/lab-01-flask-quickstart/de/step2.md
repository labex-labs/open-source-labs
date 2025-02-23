# Ein einfachen Route erstellen

Routes in Flask definieren die URL-Muster für Ihre Anwendung. Lassen Sie uns einen einfachen Route erstellen, der eine "Hello, World!"-Nachricht anzeigt.

1. Fügen Sie den folgenden Code in Ihre `app.py`-Datei hinzu:

   ```python
   @app.route("/")
   def hello_world():
       return "Hello, World!"
   ```

2. Speichern Sie die Datei.
