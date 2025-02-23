# Inclut les fichiers nécessaires

Le build backend de setuptools a besoin d'un autre fichier nommé `MANIFEST.in` pour inclure les fichiers non-Python dans le projet.

Crée un `MANIFEST.in` avec le contenu suivant :

```none
# MANIFEST.in

include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

Cela indique au build de copier tout ce qui se trouve dans les répertoires `static` et `templates`, ainsi que le fichier `schema.sql`, tout en excluant tous les fichiers de bytecode.
