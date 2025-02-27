# Générer des données

La première étape consiste à générer quelques données d'exemple que nous pouvons utiliser pour entraîner et tester notre modèle. Nous utiliserons la fonction `make_classification` du module `sklearn.datasets` pour générer un problème de classification binaire aléatoire avec 3 caractéristiques informatives.

```python
import numpy as np
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=3, n_informative=3,
                           n_redundant=0, n_classes=2, random_state=1)
```
