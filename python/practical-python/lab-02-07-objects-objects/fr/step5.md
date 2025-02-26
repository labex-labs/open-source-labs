# Identité et références

Utilisez l'opérateur `is` pour vérifier si deux valeurs sont exactement le même objet.

```python
>>> a = [1,2,3]
>>> b = a
>>> a is b
True
>>>
```

`is` compare l'identité de l'objet (un entier). L'identité peut être obtenue en utilisant `id()`.

```python
>>> id(a)
3588944
>>> id(b)
3588944
>>>
```

Note : Il est presque toujours préférable d'utiliser `==` pour vérifier des objets. Le comportement de `is` est souvent inattendu :

```python
>>> a = [1,2,3]
>>> b = a
>>> c = [1,2,3]
>>> a is b
True
>>> a is c
False
>>> a == c
True
>>>
```
