# Générateurs

Un générateur est une fonction qui définit une itération.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

Par exemple :

```python
>>> for x in countdown(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```

Un générateur est toute fonction qui utilise l'instruction `yield`.

Le comportement des générateurs est différent d'une fonction normale. Appeler une fonction génératrice crée un objet générateur. Elle n'exécute pas immédiatement la fonction.

```python
def countdown(n):
    # Ajout d'une instruction print
    print('Compte à rebours depuis', n)
    while n > 0:
        yield n
        n -= 1
```

```python
>>> x = countdown(10)
# Il n'y a AUCUNE INSTRUCTION PRINT
>>> x
# x est un objet générateur
<generator object at 0x58490>
>>>
```

La fonction n'est exécutée que lors de l'appel à `__next__()`.

```python
>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>> x.__next__()
Compte à rebours depuis 10
10
>>>
```

`yield` produit une valeur, mais suspend l'exécution de la fonction. La fonction reprend lors du prochain appel à `__next__()`.

```python
>>> x.__next__()
9
>>> x.__next__()
8
```

Lorsque le générateur renvoie finalement, l'itération lève une erreur.

```python
>>> x.__next__()
1
>>> x.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in? StopIteration
>>>
```

_Attention : Une fonction génératrice implémente le même protocole de bas niveau que les instructions for utilisées sur les listes, les tuples, les dictionnaires, les fichiers, etc._
