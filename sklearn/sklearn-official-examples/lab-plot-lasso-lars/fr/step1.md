# Charger les données

La première étape consiste à charger l'ensemble de données du diabète à partir de Scikit-Learn.

```python
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
```
