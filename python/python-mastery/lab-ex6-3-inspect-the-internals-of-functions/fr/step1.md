# Inspecter les fonctions

Définissez une fonction simple :

```python
>>> def add(x,y):
       'Adds two things'
       return x+y

>>>
```

Faites un `dir()` sur la fonction pour examiner ses attributs.

```python
>>> dir(add)
... regardez le résultat...
>>>
```

Obtenez des informations de base telles que le nom de la fonction, le nom du module de définition et la chaîne de documentation.

```python
>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>> add.__doc__
'Adds two things'
>>>
```

L'attribut `__code__` d'une fonction contient des informations de bas niveau sur l'implémentation de la fonction. Essayez de regarder cela et de déterminer le nombre d'arguments requis et les noms des variables locales.
