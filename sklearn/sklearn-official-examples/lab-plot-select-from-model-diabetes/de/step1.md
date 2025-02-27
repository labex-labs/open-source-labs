# Laden der Daten

Wir laden den Diabetes-Datensatz aus scikit-learn und drucken seine Beschreibung.

```python
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
print(diabetes.DESCR)
```
