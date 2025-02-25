# Exercice 2.14 : Plus d'opérations sur les séquences

Expérimentez de manière interactive certaines des opérations de réduction de séquence.

```python
>>> data = [4, 9, 1, 25, 16, 100, 49]
>>> min(data)
1
>>> max(data)
100
>>> sum(data)
204
>>>
```

Essayez de parcourir les données.

```python
>>> for x in data:
        print(x)

4
9
...
>>> for n, x in enumerate(data):
        print(n, x)

0 4
1 9
2 1
...
>>>
```

Parfois, les débutants utilisent la structure `for`, la fonction `len()` et la fonction `range()` dans un fragment de code horrible qui semble sortir des profondeurs d'un programme C rouillé.

```python
>>> for n in range(len(data)):
        print(data[n])

4
9
1
...
>>>
```

Ne faites pas ça! Non seulement ça fait mal aux yeux de tout le monde de le lire, mais c'est inefficace en termes de mémoire et ça exécute beaucoup plus lentement. Utilisez simplement une boucle `for` normale si vous voulez parcourir des données. Utilisez `enumerate()` si vous avez besoin de l'index pour une raison quelconque.
