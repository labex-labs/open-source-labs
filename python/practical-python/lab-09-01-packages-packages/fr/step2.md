# Packages vs Modules

Pour de plus grandes collections de code, il est courant d'organiser les modules en un package.

```code
# De cela
pcost.py
report.py
fileparse.py

# A cela
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Vous choisissez un nom et créez un répertoire de niveau supérieur. `porty` dans l'exemple ci-dessus (choisir ce nom est clairement la première étape la plus importante).

Ajoutez un fichier `__init__.py` au répertoire. Il peut être vide.

Placez vos fichiers sources dans le répertoire.
