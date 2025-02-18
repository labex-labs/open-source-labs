# Génération de données synthétiques

Ensuite, nous allons générer des données synthétiques pour démontrer la différence entre LDA et QDA. Nous utiliserons la fonction `make_classification` de scikit-learn pour créer deux classes avec des modèles distincts.

```python
from sklearn.datasets import make_classification

# Génération de données synthétiques
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=1)
```
