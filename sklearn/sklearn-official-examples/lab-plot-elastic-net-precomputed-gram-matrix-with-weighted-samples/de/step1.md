# Laden des Datensatzes und Erstellen von Stichprobengewichten

Wir beginnen mit dem Laden des Datensatzes und der Erstellung einiger Stichprobengewichte. Wir verwenden die `make_regression`-Funktion aus scikit-learn, um einen zufälligen Regressionsdatensatz mit 100.000 Stichproben zu generieren. Anschließend generieren wir einen lognormalverteilten Gewichtsvektor und normalisieren ihn, sodass die Summe der Gewichte der Gesamtzahl der Stichproben entspricht.

```python
import numpy as np
from sklearn.datasets import make_regression

rng = np.random.RandomState(0)

n_samples = int(1e5)
X, y = make_regression(n_samples=n_samples, noise=0.5, random_state=rng)

sample_weight = rng.lognormal(size=n_samples)
# normalize the sample weights
normalized_weights = sample_weight * (n_samples / (sample_weight.sum()))
```
