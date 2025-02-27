# Daten generieren

Zunächst generieren wir einen Datensatz mit 125 Proben und 2 Merkmalen. Beide Merkmale sind gaussverteilt mit einem Mittelwert von 0. Merkmal 1 hat jedoch eine Standardabweichung von 2 und Merkmal 2 hat eine Standardabweichung von 1. Anschließend ersetzen wir 25 Proben mit gaussischen Ausreißerproben, bei denen Merkmal 1 eine Standardabweichung von 1 und Merkmal 2 eine Standardabweichung von 7 hat.

```python
import numpy as np

# für konsistente Ergebnisse
np.random.seed(7)

n_samples = 125
n_outliers = 25
n_features = 2

# generiere gaussianische Daten von der Form (125, 2)
gen_cov = np.eye(n_features)
gen_cov[0, 0] = 2.0
X = np.dot(np.random.randn(n_samples, n_features), gen_cov)
# füge einige Ausreißer hinzu
outliers_cov = np.eye(n_features)
outliers_cov[np.arange(1, n_features), np.arange(1, n_features)] = 7.0
X[-n_outliers:] = np.dot(np.random.randn(n_outliers, n_features), outliers_cov)
```
