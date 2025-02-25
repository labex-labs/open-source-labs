# Opérations sur les listes

Les listes peuvent contenir des éléments de tout type. Ajoutez un nouvel élément en utilisant `append()` :

```python
names.append('Murphy')    # Ajoute à la fin
names.insert(2, 'Aretha') # Insère au milieu
```

Utilisez `+` pour concaténer des listes :

```python
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
```

Les listes sont indexées par des entiers. En commençant par 0.

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]

names[0]  # 'Elwood'
names[1]  # 'Jake'
names[2]  # 'Curtis'
```

Les indices négatifs comptent à partir de la fin.

```python
names[-1] # 'Curtis'
```

Vous pouvez modifier n'importe quel élément d'une liste.

```python
names[1] = 'Joliet Jake'
names                     # [ 'Elwood', 'Joliet Jake', 'Curtis' ]
```

Longueur de la liste.

```python
names = ['Elwood','Jake','Curtis']
len(names)  # 3
```

Test d'appartenance (`in`, `not in`).

```python
'Elwood' in names       # True
'Britney' not in names  # True
```

Réplication (`s * n`).

```python
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```
