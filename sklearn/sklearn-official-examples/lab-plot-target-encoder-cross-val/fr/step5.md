# Entraîner un régresseur Ridge avec validation croisée

Ensuite, nous allons créer un pipeline avec le `TargetEncoder` et le modèle Ridge. Le pipeline utilise `TargetEncoder.fit_transform` qui utilise la validation croisée. Exécutez le code suivant pour entraîner le modèle Ridge avec validation croisée :

```python
model_with_cv = make_pipeline(TargetEncoder(random_state=0), ridge)
model_with_cv.fit(X_train, y_train)
print("Model with CV on training set: ", model_with_cv.score(X_train, y_train))
print("Model with CV on test set: ", model_with_cv.score(X_test, y_test))
```
