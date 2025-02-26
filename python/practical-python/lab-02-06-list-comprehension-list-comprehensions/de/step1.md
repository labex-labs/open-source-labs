# Neuen Listen erstellen

Eine Listenverständnis erstellt eine neue Liste, indem eine Operation auf jedes Element einer Sequenz angewendet wird.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

Ein weiteres Beispiel:

```python
>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> a
['elwood', 'jake']
>>>
```

Die allgemeine Syntax lautet: `[ <Ausdruck> für <Variablennamen> in <Sequenz> ]`.
