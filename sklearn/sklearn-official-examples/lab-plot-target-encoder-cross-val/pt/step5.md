# Treinar um Regressor Ridge com Validação Cruzada

Em seguida, criaremos um pipeline com o modelo `TargetEncoder` e Ridge. O pipeline utiliza `TargetEncoder.fit_transform`, que usa validação cruzada. Execute o código a seguir para treinar o modelo Ridge com validação cruzada:

```python
model_with_cv = make_pipeline(TargetEncoder(random_state=0), ridge)
model_with_cv.fit(X_train, y_train)
print("Model with CV on training set: ", model_with_cv.score(X_train, y_train))
print("Model with CV on test set: ", model_with_cv.score(X_test, y_test))
```
