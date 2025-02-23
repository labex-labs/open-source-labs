# Création d'une route de base

Les routes dans Flask définissent les modèles d'URL pour votre application. Créons une route de base qui affiche un message "Bonjour, le monde!".

1. Ajoutez le code suivant à votre fichier `app.py` :

   ```python
   @app.route("/")
   def hello_world():
       return "Hello, World!"
   ```

2. Enregistrez le fichier.
