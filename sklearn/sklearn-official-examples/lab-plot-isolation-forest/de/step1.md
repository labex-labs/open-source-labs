# Datenerzeugung

Wir werden einen Datensatz mit zwei Clustern und einigen Ausreißern erzeugen. Die Cluster werden durch Zufallsstichproben aus der Standardnormalverteilung generiert. Einer von ihnen wird sphärisch sein, und der andere wird leicht deformiert sein. Die Ausreißer werden durch Zufallsstichproben aus einer Gleichverteilung generiert.

```python
import numpy as np
from sklearn.model_selection import train_test_split

n_samples, n_outliers = 120, 40
rng = np.random.RandomState(0)
covariance = np.array([[0.5, -0.1], [0.7, 0.4]])
cluster_1 = 0.4 * rng.randn(n_samples, 2) @ covariance + np.array([2, 2])  # allgemein
cluster_2 = 0.3 * rng.randn(n_samples, 2) + np.array([-2, -2])  # sphärisch
outliers = rng.uniform(low=-4, high=4, size=(n_outliers, 2))

X = np.concatenate([cluster_1, cluster_2, outliers])
y = np.concatenate(
    [np.ones((2 * n_samples), dtype=int), -np.ones((n_outliers), dtype=int)]
)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
```
