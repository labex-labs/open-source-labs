# Zufällige Daten generieren

Wir werden einige zufällige Daten generieren, um unseren Algorithmus zu testen. Wir werden 200 Stichproben mit 50 Merkmalen erstellen und für jedes Merkmal einen wahren Koeffizienten von 3 verwenden. Anschließend werden wir die Koeffizienten auf nichtnegativ begrenzen. Schließlich werden wir der Stichprobe etwas Rauschen hinzufügen.

```python
import numpy as np

np.random.seed(42)

n_samples, n_features = 200, 50
X = np.random.randn(n_samples, n_features)
true_coef = 3 * np.random.randn(n_features)
true_coef[true_coef < 0] = 0
y = np.dot(X, true_coef)
y += 5 * np.random.normal(size=(n_samples,))
```
