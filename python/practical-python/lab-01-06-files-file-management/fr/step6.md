# Exercice 1.28: Autres types de "fichiers"

Et si vous vouliez lire un fichier non texte, tel qu'un fichier de données compressé au format gzip? La fonction `open()` intégrée ne vous aidera pas ici, mais Python a un module de bibliothèque `gzip` qui peut lire les fichiers compressés au format gzip.

Essayez-le :

```python
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

... regardez la sortie...
>>>
```

Remarque : Inclure le mode de fichier `'rt'` est crucial ici. Si vous l'oubliez, vous obtiendrez des chaînes d'octets au lieu de chaînes de caractères normales.
