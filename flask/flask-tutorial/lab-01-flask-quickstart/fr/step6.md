# Ajout de contenu dynamique

Flask nous permet de passer du contenu dynamique à nos modèles. Modifions notre route pour passer un paramètre de nom et afficher un message de bienvenue personnalisé.

1. Modifiez votre fichier `app.py` pour accepter un paramètre de nom dans la route :

   ```python
   @app.route("/<name>")
   def hello(name):
       return render_template("index.html", name=name)
   ```

2. Ouvrez le fichier `index.html` et modifiez la balise `<h1>` pour afficher le message de bienvenue personnalisé :

   ```html
   <h1>Bonjour, {{ name }}!</h1>
   ```
