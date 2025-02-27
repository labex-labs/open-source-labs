# Generar el conjunto de datos Swiss Roll

Comenzamos generando el conjunto de datos Swiss Roll utilizando la función `make_swiss_roll()` de `sklearn.datasets`. Esta función genera un conjunto de datos tridimensional con una forma en espiral.

```python
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

sr_points, sr_color = datasets.make_swiss_roll(n_samples=1500, random_state=0)
```
