# Kreuzvalidierte Vorhersagen generieren

Wir werden die Funktion `cross_val_predict` aus scikit-learn verwenden, um kreuzvalidierte Vorhersagen zu generieren.

```python
from sklearn.model_selection import cross_val_predict

y_pred = cross_val_predict(lr, X, y, cv=10)
```
