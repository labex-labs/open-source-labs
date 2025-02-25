# Utilisation de fonctions raccourcies

Le module `numpy.lib.npyio` fournit des fonctions raccourcies dérivées de `numpy.genfromtxt`. Ces fonctions ont des valeurs par défaut différentes et renvoient soit un tableau NumPy standard, soit un tableau masqué.

```python
from numpy.lib.npyio import recfromtxt

recfromtxt(StringIO(data), delimiter=",")
```
