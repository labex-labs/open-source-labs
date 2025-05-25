# Operações em Listas

Listas podem conter itens de qualquer tipo. Adicione um novo item usando `append()`:

```python
names.append('Murphy')    # Adiciona ao final
names.insert(2, 'Aretha') # Insere no meio
```

Use `+` para concatenar listas:

```python
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
```

Listas são indexadas por inteiros, começando em 0.

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]

names[0]  # 'Elwood'
names[1]  # 'Jake'
names[2]  # 'Curtis'
```

Índices negativos contam do final.

```python
names[-1] # 'Curtis'
```

Você pode alterar qualquer item em uma lista.

```python
names[1] = 'Joliet Jake'
names                     # [ 'Elwood', 'Joliet Jake', 'Curtis' ]
```

Comprimento da lista.

```python
names = ['Elwood','Jake','Curtis']
len(names)  # 3
```

Teste de pertinência (`in`, `not in`).

```python
'Elwood' in names       # True
'Britney' not in names  # True
```

Replicação (`s * n`).

```python
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```
