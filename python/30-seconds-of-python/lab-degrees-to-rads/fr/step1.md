# Degrés en radians

Écrivez une fonction `degrees_to_rads(deg)` qui prend un angle en degrés en argument et renvoie l'angle en radians. Votre fonction devrait utiliser la formule suivante pour convertir les degrés en radians :

```
radians = (degrees * pi) / 180.0
```

où `pi` est une valeur constante représentant le rapport de la circonférence d'un cercle à son diamètre (environ 3,14159).

Votre fonction devrait renvoyer l'angle en radians arrondi à 4 décimales.

```python
from math import pi

def degrees_to_rads(deg):
  return (deg * pi) / 180.0
```

```python
degrees_to_rads(180) # ~3.1416
```
