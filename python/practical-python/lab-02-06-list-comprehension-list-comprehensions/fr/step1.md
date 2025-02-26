# Création de nouvelles listes

Une compréhension de liste crée une nouvelle liste en appliquant une opération à chaque élément d'une séquence.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

Un autre exemple :

```python
>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> a
['elwood', 'jake']
>>>
```

La syntaxe générale est : `[ <expression> for <variable_name> in <sequence> ]`.
