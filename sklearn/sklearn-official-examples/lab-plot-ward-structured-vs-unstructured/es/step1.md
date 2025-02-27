# Generar datos

Comenzamos generando el conjunto de datos Swiss Roll utilizando la función `make_swiss_roll` de Scikit-learn. El conjunto de datos Swiss Roll es un conjunto de datos tridimensional con una forma en espiral.

```python
from sklearn.datasets import make_swiss_roll

n_samples = 1500
noise = 0.05
X, _ = make_swiss_roll(n_samples, noise=noise)
# Hacerlo más delgado
X[:, 1] *= 0.5
```
