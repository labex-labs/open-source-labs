# Défi d'API : Avertissements de type

Les fonctions peuvent avoir des avertissements de type optionnels attachés aux arguments et aux valeurs de retour. Par exemple :

```python
def add(x:int, y:int) -> int:
    return x + y
```

Le module `typing` a des classes supplémentaires pour exprimer des types plus complexes, y compris des conteneurs. Par exemple :

```python
from typing import List

def sum_squares(nums: List[int]) -> int:
    total = 0
    for n in nums:
        total += n*n
    return total
```

Votre défi : Modifiez le code dans `reader.py` de sorte que toutes les fonctions aient des avertissements de type. Essayez de rendre les avertissements de type le plus précis possible. Pour ce faire, vous devrez peut-être consulter la documentation du [module typing](https://docs.python.org/3/library/typing.html).
