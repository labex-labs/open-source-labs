# Datensatz

Zunächst werden wir den Diabetes-Datensatz mithilfe der Funktion `load_diabetes` aus `sklearn.datasets` laden. Der Datensatz besteht aus 10 Basisvariablen, Alter, Geschlecht, Körpermasseindex, durchschnittlicher Blutdruck und sechs Blutserummessungen sowie einer quantitativen Messung der Krankheitsentwicklung ein Jahr nach der Basis.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
X.head()
```
