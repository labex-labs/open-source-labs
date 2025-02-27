# Lasso-Pfad berechnen

Als nächstes berechnen wir den Lasso-Pfad mithilfe des LARS-Algorithmus. Die `lars_path`-Funktion aus dem `linear_model`-Modul von Scikit-Learn wird verwendet, um den Lasso-Pfad zu berechnen. Die Funktion nimmt die Eingabefeatures, die Zielvariable und die Methode als Parameter entgegen. In diesem Fall verwenden wir die Methode "lasso" für die L1-Regularisierung.

```python
from sklearn import linear_model

_, _, coefs = linear_model.lars_path(X, y, method="lasso", verbose=True)
```
