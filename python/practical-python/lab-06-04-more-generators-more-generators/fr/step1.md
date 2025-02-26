# Expressions de générateur

Une version génératrice d'une compréhension de liste.

```python
>>> a = [1,2,3,4]
>>> b = (2*x for x in a)
>>> b
<generator object at 0x58760>
>>> for i in b:
...   print(i, end=' ')
...
2 4 6 8
>>>
```

Différences avec les Compréhensions de liste.

- Ne construit pas une liste.
- Son seul usage utile est l'itération.
- Une fois consommée, ne peut pas être réutilisée.

Syntaxe générale.

```python
(<expression> for i in s if <conditional>)
```

Elle peut également servir comme argument de fonction.

```python
sum(x*x for x in a)
```

Elle peut être appliquée à tout itérable.

```python
>>> a = [1,2,3,4]
>>> b = (x*x for x in a)
>>> c = (-x for x in b)
>>> for i in c:
...   print(i, end=' ')
...
-1 -4 -9 -16
>>>
```

L'utilisation principale des expressions de générateur est dans le code qui effectue un certain calcul sur une séquence, mais n'utilise le résultat qu'une seule fois. Par exemple, supprimer tous les commentaires d'un fichier.

```python
f = open('somefile.txt')
lines = (line for line in f if not line.startswith('#'))
for line in lines:
  ...
f.close()
```

Avec les générateurs, le code s'exécute plus rapidement et utilise peu de mémoire. C'est comme un filtre appliqué à un flux.
