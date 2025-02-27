# Générer des données aléatoires

Tout d'abord, nous devons générer des données aléatoires avec une caractéristique discriminante et des caractéristiques bruitées. Nous utiliserons la fonction `make_blobs` de scikit-learn pour générer deux grappes de données avec une caractéristique discriminante. Ensuite, nous ajouterons du bruit aléatoire aux autres caractéristiques.

```python
import numpy as np
from sklearn.datasets import make_blobs

def generate_data(n_samples, n_features):
    """Générer des données aléatoires ressemblant à des grappes avec des caractéristiques bruitées.

    Cela renvoie un tableau de données d'entrée de forme `(n_samples, n_features)`
    et un tableau d'étiquettes cibles de `n_samples`.

    Seule une caractéristique contient des informations discriminantes, les autres caractéristiques
    ne contiennent que du bruit.
    """
    X, y = make_blobs(n_samples=n_samples, n_features=1, centers=[[-2], [2]])

    # ajouter des caractéristiques non discriminantes
    if n_features > 1:
        X = np.hstack([X, np.random.randn(n_samples, n_features - 1)])
    return X, y
```
