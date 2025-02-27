# Entraîner un régresseur Ridge sans validation croisée

Alors que `TargetEncoder.fit_transform` utilise la validation croisée par intervalle, `TargetEncoder.transform` lui-même ne réalise pas de validation croisée. Il utilise l'agrégation de l'ensemble d'entraînement complet pour transformer les caractéristiques catégorielles. Ainsi, nous pouvons utiliser `TargetEncoder.fit` suivi de `TargetEncoder.transform` pour désactiver la validation croisée. Cette codification est ensuite passée au modèle Ridge. Exécutez le code suivant pour entraîner le modèle Ridge sans validation croisée :

```python
target_encoder = TargetEncoder(random_state=0)
target_encoder.fit(X_train, y_train)
X_train_no_cv_encoding = target_encoder.transform(X_train)
X_test_no_cv_encoding = target_encoder.transform(X_test)

model_no_cv = ridge.fit(X_train_no_cv_encoding, y_train)
print(
    "Model without CV on training set: ",
    model_no_cv.score(X_train_no_cv_encoding, y_train),
)
print(
    "Model without CV on test set: ", model_no_cv.score(X_test_no_cv_encoding, y_test)
)
```
