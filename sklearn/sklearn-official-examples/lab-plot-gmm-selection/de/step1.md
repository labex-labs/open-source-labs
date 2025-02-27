# Datenerzeugung

Wir generieren zwei Komponenten (jedoch eine enthält `n_samples`), indem wir die Standardnormalverteilung zufällig abprobieren, wie von `numpy.random.randn` zurückgegeben. Eine Komponente bleibt sphärisch, wird jedoch verschoben und neu skaliert. Die andere wird deformiert, um eine allgemeinere Kovarianzmatrix zu haben.

```python
import numpy as np

n_samples = 500
np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
component_1 = np.dot(np.random.randn(n_samples, 2), C)  # allgemein
component_2 = 0.7 * np.random.randn(n_samples, 2) + np.array([-4, 1])  # sphärisch

X = np.concatenate([component_1, component_2])
```
