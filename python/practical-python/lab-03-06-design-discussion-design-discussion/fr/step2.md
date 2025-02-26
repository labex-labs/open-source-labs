# Idée profonde : "Duck Typing"

[Duck Typing](https://en.wikipedia.org/wiki/Duck_typing) est un concept de programmation informatique pour déterminer si un objet peut être utilisé à une fin particulière. C'est une application du [test canard](https://en.wikipedia.org/wiki/Duck_test).

> Si ça ressemble à un canard, nage comme un canard et canarde comme un canard, alors c'est probablement un canard.

Dans la deuxième version de `read_data()` ci-dessus, la fonction attend n'importe quel objet itérable. Pas seulement les lignes d'un fichier.

```python
def read_data(lines):
    records = []
    for line in lines:
     ...
        records.append(r)
    return records
```

Cela signifie que nous pouvons l'utiliser avec d'autres _lignes_.

```python
# Un fichier CSV
lines = open('data.csv')
data = read_data(lines)

# Un fichier compressé au format zip
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# L'entrée standard
lines = sys.stdin
data = read_data(lines)

# Une liste de chaînes de caractères
lines = ['ACME,50,91.1','IBM,75,123.45',...]
data = read_data(lines)
```

Il y a une flexibilité considérable avec cette conception.

_Question : Devrions-nous accepter ou combattre cette flexibilité?_
