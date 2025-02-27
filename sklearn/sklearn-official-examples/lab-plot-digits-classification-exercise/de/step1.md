# Lade den Digits-Datensatz

Wir beginnen, indem wir den Digits-Datensatz mit der Funktion `load_digits` aus scikit-learn laden. Diese Funktion gibt zwei Arrays zurück: `X_digits`, das die Eingabedaten enthält, und `y_digits`, das die Ziel-Labels enthält.

```python
from sklearn import datasets

X_digits, y_digits = datasets.load_digits(return_X_y=True)
```
