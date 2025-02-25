# Filtrer les valeurs uniques d'une liste

Écrivez une fonction Python appelée `filter_unique(lst)` qui prend une liste en argument et renvoie une nouvelle liste ne contenant que les valeurs non uniques. Pour résoudre ce problème, vous pouvez suivre les étapes suivantes :

1. Utilisez `collections.Counter` pour obtenir le compte de chaque valeur dans la liste.
2. Utilisez une compréhension de liste pour créer une liste ne contenant que les valeurs non uniques.

Votre fonction doit répondre aux exigences suivantes :

- La fonction doit prendre une liste en argument.
- La fonction doit renvoyer une nouvelle liste ne contenant que les valeurs non uniques.
- La fonction ne doit pas modifier la liste d'origine.
- La fonction doit être sensible à la casse, ce qui signifie que 'a' et 'A' sont considérées comme des valeurs différentes.

```python
def filter_unique(lst):
    # votre code ici
```

```python
from collections import Counter

def filter_unique(lst):
  return [item for item, count in Counter(lst).items() if count > 1]
```

```python
filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]
```
