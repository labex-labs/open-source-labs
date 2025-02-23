# Ajout de modèles HTML

Flask utilise des modèles Jinja2 pour générer du contenu HTML. Créons un fichier de modèle et le rendons dans notre route.

1. Créez un nouveau répertoire dans votre projet appelé `templates`.

2. Dans le répertoire `templates`, créez un nouveau fichier appelé `index.html`.

3. Ouvrez le fichier `index.html` et ajoutez le code HTML suivant :

   ```html
   <!doctype html>
   <html>
     <head>
       <title>Flask Quickstart</title>
     </head>
     <body>
       <h1>Bonjour, Flask!</h1>
     </body>
   </html>
   ```

4. Modifiez votre fichier `app.py` pour rendre le modèle `index.html` :

   ```python
   from flask import render_template

   @app.route("/")
   def hello_world():
       return render_template("index.html")
   ```
