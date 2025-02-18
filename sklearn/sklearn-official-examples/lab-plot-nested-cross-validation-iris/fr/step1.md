# Charger le jeu de données

La première étape consiste à charger le jeu de données iris à partir de scikit-learn.

```python
from sklearn.datasets import load_iris

# Charger le jeu de données
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
```
