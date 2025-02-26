# Vérification

Modifiez la classe `ValidatedFunction` de manière à imposer les vérifications de valeur attachées via les annotations de fonction. Par exemple :

```python
>>> def add(x: Integer, y:Integer):
        return x + y
>>> add = ValidatedFunction(add)
>>> add(2,3)
5
>>> add('two','three')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 67, in __call__
    self.func.__annotations__[name].check(val)
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: expected <class 'int'>
>>>>
```

Indice : Pour ce faire, experimentez avec la liaison de signature. Utilisez la méthode `bind()` des objets `Signature` pour lier les arguments de fonction aux noms d'arguments. Ensuite, croyez cette information avec l'attribut `__annotations__` pour obtenir les différentes classes de validateur.

Gardez à l'esprit que vous créez un objet qui ressemble à une fonction, mais qui n'en est pas vraiment. Il y a de la magie qui se passe en coulisses.
