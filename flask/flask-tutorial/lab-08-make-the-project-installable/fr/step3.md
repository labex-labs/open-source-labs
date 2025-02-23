# Installe le projet

Ensuite, nous allons utiliser `pip` pour installer le projet dans l'environnement virtuel.

Exécutez la commande suivante dans votre terminal :

```none
pip install -e.
```

Cela indique à pip de trouver `pyproject.toml` dans le répertoire actuel et d'installer le projet en mode éditable ou de développement. Le mode éditable signifie que lorsque vous apportez des modifications à votre code local, vous n'aurez besoin de réinstaller que si vous modifiez les métadonnées du projet.

Pour vérifier l'installation, utilisez la commande `pip list` :

```none
pip list
```

La sortie devrait montrer le projet installé et ses dépendances.
