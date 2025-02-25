# Création d'un tableau structuré

Pour créer un tableau structuré, nous pouvons utiliser la fonction `np.array` et spécifier le type de données à l'aide du paramètre `dtype`. Le type de données doit être une liste de tuples, où chaque tuple représente un champ dans le tableau structuré. Chaque tuple doit contenir le nom du champ et le type de données du champ.

```python
import numpy as np

# Crée un tableau structuré
x = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
