# Daten generieren

Wir beginnen, indem wir den Swiss Roll-Datensatz mit der Funktion `make_swiss_roll` aus Scikit-learn generieren. Der Swiss Roll-Datensatz ist ein 3D-Datensatz mit einer spiralförmigen Gestalt.

```python
from sklearn.datasets import make_swiss_roll

n_samples = 1500
noise = 0.05
X, _ = make_swiss_roll(n_samples, noise=noise)
# Make it thinner
X[:, 1] *= 0.5
```
