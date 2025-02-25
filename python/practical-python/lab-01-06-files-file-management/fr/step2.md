# Idiomes courants pour la lecture des données de fichiers

Lire un fichier entier d'un coup sous forme de chaîne de caractères.

```python
with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` est une chaîne de caractères contenant tout le texte de `foo.txt`
```

Lire un fichier ligne par ligne en itérant.

```python
with open(filename, 'rt') as file:
    for line in file:
        # Traiter la ligne
```
