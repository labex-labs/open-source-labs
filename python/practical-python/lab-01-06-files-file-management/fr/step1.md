# Entrée et sortie de fichiers

Ouvrir un fichier.

```python
f = open('foo.txt', 'rt')     # Ouvrir pour la lecture (texte)
g = open('bar.txt', 'wt')     # Ouvrir pour l'écriture (texte)
```

Lire tout le contenu.

```python
data = f.read()

# Lire seulement jusqu'à 'maxbytes' octets
data = f.read([maxbytes])
```

Écrire du texte.

```python
g.write('some text')
```

Fermer le fichier une fois terminé.

```python
f.close()
g.close()
```

Il est important de fermer correctement les fichiers, mais il est facile d'oublier cette étape. Ainsi, l'approche préférée est d'utiliser l'instruction `with` de cette manière.

```python
with open(filename, 'rt') as file:
    # Utiliser le fichier `file`
  ...
    # Pas besoin de fermer explicitement
...instructions
```

Cela ferme automatiquement le fichier lorsque le contrôle quitte le bloc de code indenté.
