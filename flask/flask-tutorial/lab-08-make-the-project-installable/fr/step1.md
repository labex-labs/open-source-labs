# Décris le projet

Tout d'abord, nous devons créer un fichier `pyproject.toml` pour décrire notre projet et la manière de le construire.

Le fichier `pyproject.toml` devrait ressembler à ceci :

```toml
# pyproject.toml

[project]
name = "flaskr" # nom du projet
version = "1.0.0" # version du projet
dependencies = [
    "flask", # dépendances du projet
]

[build-system]
requires = ["setuptools"] # système de build requis
build-backend = "setuptools.build_meta" # système de build de fond
```
