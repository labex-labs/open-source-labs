# Définissez l'estimateur et la grille de paramètres

Maintenant, nous devons définir l'estimateur que nous voulons ajuster et la grille de paramètres que nous voulons explorer. La grille de paramètres spécifie les valeurs que nous voulons essayer pour chaque hyperparamètre.

```python
from sklearn.svm import SVC

# Créez une instance du classifieur à vecteurs de support
svc = SVC()

# Définissez la grille de paramètres
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 0.01, 0.001], 'kernel': ['linear', 'rbf']}
```
