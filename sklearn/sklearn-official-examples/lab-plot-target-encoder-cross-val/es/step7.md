# Entrenar un regresor Ridge sin validación cruzada

Mientras que `TargetEncoder.fit_transform` utiliza validación cruzada por intervalos, `TargetEncoder.transform` en sí mismo no realiza ninguna validación cruzada. Utiliza la agregación del conjunto de entrenamiento completo para transformar las características categóricas. Por lo tanto, podemos usar `TargetEncoder.fit` seguido de `TargetEncoder.transform` para deshabilitar la validación cruzada. Esta codificación se pasa luego al modelo Ridge. Ejecute el siguiente código para entrenar el modelo Ridge sin validación cruzada:

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
