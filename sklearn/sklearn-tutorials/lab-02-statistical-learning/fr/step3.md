# Objets estimateurs

Les objets estimateurs dans scikit-learn sont utilisés pour apprendre à partir de données et faire des prédictions. Ils peuvent être des algorithmes de classification, de régression ou de regroupement, ou des transformateurs qui extraient des caractéristiques utiles à partir de données brutes. Créons un exemple simple d'un objet estimateur :

```python
from sklearn.base import BaseEstimator

class Estimator(BaseEstimator):
    def __init__(self, param1=0, param2=0):
        self.param1 = param1
        self.param2 = param2

    def fit(self, data):
        # Implémentation de la méthode fit
        pass

estimator = Estimator()
```
