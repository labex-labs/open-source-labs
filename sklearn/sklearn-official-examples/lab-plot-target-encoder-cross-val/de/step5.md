# Training eines Ridge-Regressors mit Kreuzvalidierung

Als Nächstes werden wir eine Pipeline (Pipeline) mit dem `TargetEncoder` und dem Ridge-Modell erstellen. Die Pipeline verwendet `TargetEncoder.fit_transform`, das Kreuzvalidierung nutzt. Führen Sie den folgenden Code aus, um das Ridge-Modell mit Kreuzvalidierung zu trainieren:

```python
model_with_cv = make_pipeline(TargetEncoder(random_state=0), ridge)
model_with_cv.fit(X_train, y_train)
print("Model with CV on training set: ", model_with_cv.score(X_train, y_train))
print("Model with CV on test set: ", model_with_cv.score(X_test, y_test))
```
