# Copies superficielles

Les listes et les dictionnaires ont des méthodes pour effectuer des copies.

```python
>>> a = [2,3,[100,101],4]
>>> b = list(a) # Effectuez une copie
>>> a is b
False
```

C'est une nouvelle liste, mais les éléments de la liste sont partagés.

```python
>>> a[2].append(102)
>>> b[2]
[100,101,102]
>>>
>>> a[2] is b[2]
True
>>>
```

Par exemple, la liste interne `[100, 101, 102]` est partagée. Ceci est connu sous le nom de copie superficielle. Voici une illustration.

![Copie superficielle](../assets/shallow.png)
