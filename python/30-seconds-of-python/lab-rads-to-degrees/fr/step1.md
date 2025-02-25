# Radians en degrés

Écrivez une fonction Python appelée `rads_to_degrees` qui prend un seul argument `rad`, qui est un nombre à virgule flottante représentant un angle en radians. La fonction devrait renvoyer l'angle en degrés sous forme de nombre à virgule flottante. Vous pouvez utiliser la formule suivante pour convertir un angle de radians en degrés :

```
degrees = radians * (180 / pi)
```

où `pi` est une valeur constante représentant le rapport de la circonférence d'un cercle à son diamètre, qui est approximativement égal à 3,14159.

Votre fonction devrait importer la constante `pi` à partir du module `math`.

```python
from math import pi

def rads_to_degrees(rad):
  return (rad * 180.0) / pi
```

```python
from math import pi

rads_to_degrees(pi / 2) # 90.0
```
