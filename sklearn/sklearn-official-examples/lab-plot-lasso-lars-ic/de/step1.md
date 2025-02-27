# Daten laden

Wir werden den Diabetes-Datensatz aus scikit-learn mit der load_diabetes-Methode laden.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
```
