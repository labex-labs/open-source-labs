# Générer l'ensemble de données Swiss Roll

Nous commençons par générer l'ensemble de données Swiss Roll en utilisant la fonction `make_swiss_roll()` de `sklearn.datasets`. Cette fonction génère un ensemble de données 3D avec une forme en spirale.

```python
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

sr_points, sr_color = datasets.make_swiss_roll(n_samples=1500, random_state=0)
```
