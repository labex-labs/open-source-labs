# Chargement des données

Nous chargeons l'ensemble de données Diabetes à partir de scikit-learn et affichons sa description.

```python
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
print(diabetes.DESCR)
```
