# Créez des données

Créez un tableau de valeurs comprises entre 0 et 15 avec un pas de 0,01, puis convertissez-les en radians à l'aide de la fonction radians du package basic_units.

```python
from basic_units import radians
x = [val*radians for val in np.arange(0, 15, 0.01)]
```
