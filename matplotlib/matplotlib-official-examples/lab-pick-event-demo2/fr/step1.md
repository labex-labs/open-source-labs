# Générer des données aléatoires

Tout d'abord, nous devons générer 100 jeux de données aléatoires, chacun contenant 1000 nombres aléatoires compris entre 0 et 1. Nous utiliserons le module `random` de `numpy` pour générer les données aléatoires.

```python
import numpy as np

np.random.seed(19680801)

X = np.random.rand(100, 1000)
```
