# Hinzufügen von HTML-Vorlagen

Flask verwendet Jinja2-Vorlagen, um HTML-Inhalte zu generieren. Lassen Sie uns eine Vorlagen-Datei erstellen und sie in unserem Route rendern.

1. Erstellen Sie im Projekt ein neues Verzeichnis namens `templates`.

2. Erstellen Sie im Verzeichnis `templates` eine neue Datei namens `index.html`.

3. Öffnen Sie die Datei `index.html` und fügen Sie den folgenden HTML-Code hinzu:

   ```html
   <!doctype html>
   <html>
     <head>
       <title>Flask Quickstart</title>
     </head>
     <body>
       <h1>Hello, Flask!</h1>
     </body>
   </html>
   ```

4. Ändern Sie Ihre `app.py`-Datei, um die `index.html`-Vorlage zu rendern:

   ```python
   from flask import render_template

   @app.route("/")
   def hello_world():
       return render_template("index.html")
   ```
