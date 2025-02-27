# Entraîner et évaluer le modèle de diffusion d'étiquettes

Dans cette étape, nous allons utiliser la diffusion d'étiquettes sur 20 % des données étiquetées. Nous allons sélectionner au hasard 20 % des données étiquetées, entraîner le modèle sur ces données, puis utiliser le modèle pour prédire les étiquettes pour les données non étiquetées restantes.

```python
# Entraîner et évaluer le pipeline de diffusion d'étiquettes
ls_pipeline.fit(X_train, y_train)
y_pred = ls_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
