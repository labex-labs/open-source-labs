# Exécution du serveur de développement à partir de Python

En plus d'utiliser la commande CLI Flask, vous pouvez également démarrer le serveur de développement à partir du code Python. Ajoutez le code suivant à la fin de votre fichier `app.py` :

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Maintenant, vous pouvez exécuter le serveur de développement en exécutant le fichier `app.py` avec Python :

```bash
python app.py
```

Cela lancera le serveur de développement et vous pourrez accéder à votre application Flask de la même manière que précédemment.
