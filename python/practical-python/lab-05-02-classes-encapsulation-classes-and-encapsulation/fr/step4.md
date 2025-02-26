# Attributs privés

Tout nom d'attribut commençant par `_` est considéré comme _privé_.

```python
class Person(object):
    def __init__(self, name):
        self._name = 0
```

Comme mentionné précédemment, il s'agit seulement d'un style de programmation. Vous pouvez toujours y accéder et le modifier.

```python
>>> p = Person('Guido')
>>> p._name
'Guido'
>>> p._name = 'Dave'
>>>
```

En règle générale, tout nom commençant par `_` est considéré comme une implémentation interne, que ce soit une variable, une fonction ou un nom de module. Si vous vous trouvez utiliser directement de tels noms, vous faites probablement quelque chose de mal. Recherchez une fonctionnalité de niveau supérieur.
