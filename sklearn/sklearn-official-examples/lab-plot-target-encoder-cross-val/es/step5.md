# Entrenar un regresor Ridge con validación cruzada

A continuación, crearemos un pipeline con el `TargetEncoder` y el modelo Ridge. El pipeline utiliza `TargetEncoder.fit_transform` que utiliza validación cruzada. Ejecute el siguiente código para entrenar el modelo Ridge con validación cruzada:

```python
model_with_cv = make_pipeline(TargetEncoder(random_state=0), ridge)
model_with_cv.fit(X_train, y_train)
print("Model with CV on training set: ", model_with_cv.score(X_train, y_train))
print("Model with CV on test set: ", model_with_cv.score(X_test, y_test))
```
