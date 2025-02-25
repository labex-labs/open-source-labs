# Listenoperationen

Listen können Elemente beliebigen Typs enthalten. Fügen Sie ein neues Element hinzu, indem Sie `append()` verwenden:

```python
names.append('Murphy')    # Fügt am Ende hinzu
names.insert(2, 'Aretha') # Fügt in die Mitte ein
```

Verwenden Sie `+`, um Listen zu konkatenieren:

```python
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
```

Listen werden durch ganzzahlige Indizes indiziert. Beginnend bei 0.

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]

names[0]  # 'Elwood'
names[1]  # 'Jake'
names[2]  # 'Curtis'
```

Negative Indizes zählen von der Endposition aus.

```python
names[-1] # 'Curtis'
```

Sie können jedes Element in einer Liste ändern.

```python
names[1] = 'Joliet Jake'
names                     # [ 'Elwood', 'Joliet Jake', 'Curtis' ]
```

Länge der Liste.

```python
names = ['Elwood','Jake','Curtis']
len(names)  # 3
```

Mitgliedschaftstest (`in`, `not in`).

```python
'Elwood' in names       # True
'Britney' not in names  # True
```

Replikation (`s * n`).

```python
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```
