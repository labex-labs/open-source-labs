# Entraîner et évaluer le modèle d'auto-apprentissage

Dans cette étape, nous allons utiliser l'auto-apprentissage sur 20 % des données étiquetées. Nous allons sélectionner au hasard 20 % des données étiquetées, entraîner le modèle sur ces données, puis utiliser le modèle pour prédire les étiquettes pour les données non étiquetées restantes.

```python
import numpy as np

# Sélectionner 20 % des données d'entraînement
y_mask = np.random.rand(len(y_train)) < 0.2
X_20, y_20 = map(
    list, zip(*((x, y) for x, y, m in zip(X_train, y_train, y_mask) if m))
)

# Définir le sous-ensemble non masqué comme étant non étiqueté
y_train[~y_mask] = -1

# Entraîner et évaluer le pipeline d'auto-apprentissage
st_pipeline.fit(X_train, y_train)
y_pred = st_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
