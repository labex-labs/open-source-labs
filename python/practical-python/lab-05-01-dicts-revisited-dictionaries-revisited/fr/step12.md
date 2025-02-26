# Ordre de résolution des méthodes ou MRO

Python calcule à l'avance une chaîne d'héritage et la stocke dans l'attribut _MRO_ de la classe. Vous pouvez la visualiser.

```python
>>> E.__mro__
(<class '__main__.E'>, <class '__main__.D'>,
 <class '__main__.B'>, <class '__main__.A'>,
 <type 'object'>)
>>>
```

Cette chaîne est appelée **Ordre de résolution des méthodes**. Pour trouver un attribut, Python parcourt l'ordre MRO. Le premier match remporte le combat.
