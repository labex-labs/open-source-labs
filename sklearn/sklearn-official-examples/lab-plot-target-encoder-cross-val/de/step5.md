# Trainieren eines Ridge-Regressors mit Cross-Validation

Als nächstes werden wir einen Pipeline erstellen, die den `TargetEncoder` und das Ridge-Modell enthält. Die Pipeline verwendet `TargetEncoder.fit_transform`, das Cross-Validation nutzt. Führen Sie den folgenden Code aus, um das Ridge-Modell mit Cross-Validation zu trainieren:

```python
model_with_cv = make_pipeline(TargetEncoder(random_state=0), ridge)
model_with_cv.fit(X_train, y_train)
print("Model with CV on training set: ", model_with_cv.score(X_train, y_train))
print("Model with CV on test set: ", model_with_cv.score(X_test, y_test))
```