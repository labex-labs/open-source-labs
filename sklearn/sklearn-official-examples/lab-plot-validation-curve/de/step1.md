# Laden des Datensatzes

Wir beginnen, indem wir den Digits-Datensatz aus scikit-learn laden und einen Teilsatz der Daten für die binäre Klassifizierung der Ziffern 1 und 2 auswählen.

```python
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
subset_mask = np.isin(y, [1, 2])  # binary classification: 1 vs 2
X, y = X[subset_mask], y[subset_mask]
```
