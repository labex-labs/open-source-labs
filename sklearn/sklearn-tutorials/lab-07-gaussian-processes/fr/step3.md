# Classification par processus gaussien (GPC)

La classe GaussianProcessClassifier implémente la GPC pour la classification probabiliste. Elle place une loi a priori de processus gaussien sur une fonction latente, qui est ensuite aplatie à travers une fonction de liaison pour obtenir les probabilités de classe. La GPC prend en charge la classification multi-classe en effectuant soit un contre-tous ou un contre-un basé sur l'entraînement et la prédiction.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.gaussian_process import GaussianProcessClassifier
# Créez un modèle GPC avec un noyau RBF
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Ajustez le modèle aux données d'entraînement
model.fit(X_train, y_train)

# Faites des prédictions à l'aide du modèle entraîné
y_pred = model.predict(X_test)
```
