# Charger l'ensemble de données et le prétraiter

Nous utiliserons la bibliothèque scikit-learn pour charger l'ensemble de données Iris. L'ensemble de données contient 3 classes de 50 instances chacune, où chaque classe fait référence à un type de plante d'iris. Chaque instance a 4 caractéristiques : longueur du sépale, largeur du sépale, longueur des pétales et largeur des pétales.

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay

# charger l'ensemble de données Iris
iris = datasets.load_iris()
X = iris.data[:, :2]  # nous ne prenons que les deux premières caractéristiques.
Y = iris.target
```
