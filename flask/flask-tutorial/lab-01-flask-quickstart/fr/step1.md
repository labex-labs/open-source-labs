# Configuration de Flask

Pour commencer avec Flask, vous devez l'installer et configurer un nouveau projet. Suivez les instructions ci-dessous :

1. Installez Flask en exécutant la commande suivante dans votre terminal ou invite de commandes :

   ```bash
   pip install flask
   ```

2. Ouvrez un nouveau fichier et enregistrez-le sous le nom `app.py`.

   ```bash
   cd ~/projet
   touch app.py
   ```

3. Importez le module Flask et créez une instance de la classe Flask :

   ```python
   from flask import Flask

   app = Flask(__name__)
   ```
