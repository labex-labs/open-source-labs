# List operations

Lists can hold items of any type. Add a new item using `append()`:

```python
names.append('Murphy')    # Adds at end
names.insert(2, 'Aretha') # Inserts in middle
```

Use `+` to concatenate lists:

```python
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
```

Lists are indexed by integers. Starting at 0.

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]

names[0]  # 'Elwood'
names[1]  # 'Jake'
names[2]  # 'Curtis'
```

Negative indices count from the end.

```python
names[-1] # 'Curtis'
```

You can change any item in a list.

```python
names[1] = 'Joliet Jake'
names                     # [ 'Elwood', 'Joliet Jake', 'Curtis' ]
```

Length of the list.

```python
names = ['Elwood','Jake','Curtis']
len(names)  # 3
```

Membership test (`in`, `not in`).

```python
'Elwood' in names       # True
'Britney' not in names  # True
```

Replication (`s * n`).

```python
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```
