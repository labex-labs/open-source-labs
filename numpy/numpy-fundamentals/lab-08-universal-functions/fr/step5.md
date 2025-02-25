# Règles de conversion de type

La conversion de type est effectuée sur les entrées d'une ufunc lorsqu'il n'y a pas de mise en œuvre de boucle principale pour les types d'entrée fournis. Les règles de conversion déterminent quand un type de données peut être converti en toute sécurité en un autre type de données. Voyons un exemple.

```python
import numpy as np

# Vérifiez si un entier peut être converti en toute sécurité en un nombre à virgule flottante
result = np.can_cast(np.int, np.float)

# Affichez le résultat
print(result)
```

Sortie :

```
True
```
