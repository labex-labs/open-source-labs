# Build the Application

Tout d'abord, nous devons créer un fichier wheel pour notre application. Nous allons utiliser l'outil `build` à cet effet. Installez l'outil `build` avec pip si vous ne l'avez pas déjà fait :

```bash
# Install the build tool
pip install build
```

Maintenant, utilisez l'outil `build` pour créer le fichier wheel :

```bash
# Build the wheel file
python -m build --wheel
```

Le fichier wheel devrait se trouver dans le répertoire `dist` avec un nom comme `flaskr-1.0.0-py3-none-any.whl`.
