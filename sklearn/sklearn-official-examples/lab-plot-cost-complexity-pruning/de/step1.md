# Laden der Daten

Wir werden den Brustkrebs-Datensatz aus scikit-learn verwenden. Dieser Datensatz hat 30 Merkmale und eine binäre Zielvariable, die angibt, ob ein Patient bösartigen oder gutartigen Krebs hat.

```python
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
```
