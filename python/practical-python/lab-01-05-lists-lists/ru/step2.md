# Операции со списками

Списки могут содержать элементы любого типа. Добавьте новый элемент с использованием `append()`:

```python
names.append('Murphy')    # Добавляет в конец
names.insert(2, 'Aretha') # Вставляет в середину
```

Используйте `+` для конкатенации списков:

```python
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
```

Списки индексируются целыми числами. Начиная с 0.

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]

names[0]  # 'Elwood'
names[1]  # 'Jake'
names[2]  # 'Curtis'
```

Отрицательные индексы считаются с конца.

```python
names[-1] # 'Curtis'
```

Вы можете изменить любой элемент в списке.

```python
names[1] = 'Joliet Jake'
names                     # [ 'Elwood', 'Joliet Jake', 'Curtis' ]
```

Длина списка.

```python
names = ['Elwood','Jake','Curtis']
len(names)  # 3
```

Проверка на принадлежность (`in`, `not in`).

```python
'Elwood' in names       # True
'Britney' not in names  # True
```

Дублирование (`s * n`).

```python
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```
