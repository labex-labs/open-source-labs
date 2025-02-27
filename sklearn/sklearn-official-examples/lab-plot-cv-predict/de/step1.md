# Daten laden und vorbereiten

Zunächst werden wir den Diabetes-Datensatz laden und ihn für das Modellieren vorbereiten. Wir werden die Funktion `load_diabetes` aus scikit-learn verwenden, um den Datensatz in zwei Arrays, `X` und `y`, zu laden.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)
```
