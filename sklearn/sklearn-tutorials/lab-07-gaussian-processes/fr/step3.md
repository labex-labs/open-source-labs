# Classification par processus gaussien (GPC)

La classe GaussianProcessClassifier implémente la GPC pour la classification probabiliste. Elle place une loi a priori de processus gaussien sur une fonction latente, qui est ensuite aplatie à travers une fonction de liaison pour obtenir les probabilités de classe. La GPC prend en charge la classification multi-classe en effectuant soit un contre-tous ou un contre-un basé sur l'entraînement et la prédiction.

```python
from sklearn.gaussian_process import GaussianProcessClassifier

# Créez un modèle GPC avec un noyau RBF
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Ajustez le modèle aux données d'entraînement
model.fit(X_train, y_train)

# Faites des prédictions à l'aide du modèle entraîné
y_pred = model.predict(X_test)
```
