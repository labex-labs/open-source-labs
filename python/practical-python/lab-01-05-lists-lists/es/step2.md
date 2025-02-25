# Operaciones con listas

Las listas pueden contener elementos de cualquier tipo. Agrega un nuevo elemento usando `append()`:

```python
names.append('Murphy')    # Agrega al final
names.insert(2, 'Aretha') # Inserta en el medio
```

Utiliza `+` para concatenar listas:

```python
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
```

Las listas se indexan con enteros. Comienza en 0.

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]

names[0]  # 'Elwood'
names[1]  # 'Jake'
names[2]  # 'Curtis'
```

Los índices negativos se cuentan desde el final.

```python
names[-1] # 'Curtis'
```

Puedes cambiar cualquier elemento de una lista.

```python
names[1] = 'Joliet Jake'
names                     # [ 'Elwood', 'Joliet Jake', 'Curtis' ]
```

Longitud de la lista.

```python
names = ['Elwood','Jake','Curtis']
len(names)  # 3
```

Prueba de pertenencia (`in`, `not in`).

```python
'Elwood' in names       # True
'Britney' not in names  # True
```

Replicación (`s * n`).

```python
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```
