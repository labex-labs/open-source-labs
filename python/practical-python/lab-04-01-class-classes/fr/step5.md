# Méthodes d'instance

Les méthodes d'instance sont des fonctions appliquées à des instances d'un objet.

```python
class Player:
  ...
    # `move` est une méthode
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

L'objet lui-même est toujours passé en premier argument.

```python
>>> a.move(1, 2)

# associe `a` à `self`
# associe `1` à `dx`
# associe `2` à `dy`
def move(self, dx, dy):
```

Par convention, l'instance est appelée `self`. Cependant, le nom réel utilisé n'est pas important. L'objet est toujours passé en premier argument. Il n'est que du style de programmation Python d'appeler cet argument `self`.
