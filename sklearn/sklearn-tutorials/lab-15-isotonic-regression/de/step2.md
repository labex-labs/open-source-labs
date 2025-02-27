# Erstellen von Beispiel-Daten

Als nächstes müssen wir einige Beispiel-Daten erstellen, um unser isotones Regressionsmodell anzupassen. In diesem Beispiel werden wir zwei Arrays, `X` und `y`, generieren, die die Eingabedaten und die Zielwerte darstellen, respectively.

```python
import numpy as np

# Generate random input data
np.random.seed(0)
X = np.random.rand(100)
y = 4 * X + np.random.randn(100)
```
