# Générer des données d'échantillonnage

Tout d'abord, nous allons générer quelques données d'échantillonnage pour la démonstration. Nous utiliserons l'ensemble de données iris et y ajouterons des données bruitées non corrélées.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# L'ensemble de données iris
X, y = load_iris(return_X_y=True)

# Quelques données bruitées non corrélées
E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))

# Ajoutez les données bruitées aux caractéristiques informatives
X = np.hstack((X, E))

# Divisez l'ensemble de données pour sélectionner les caractéristiques et évaluer le classifieur
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
