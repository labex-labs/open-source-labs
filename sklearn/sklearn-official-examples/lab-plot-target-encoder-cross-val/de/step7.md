# Training eines Ridge-Regressors ohne Kreuzvalidierung

Während `TargetEncoder.fit_transform` Intervall-Kreuzvalidierung verwendet, führt `TargetEncoder.transform` selbst keine Kreuzvalidierung durch. Es nutzt die Aggregation des gesamten Trainingssatzes, um die kategorischen Merkmale zu transformieren. Somit können wir `TargetEncoder.fit` gefolgt von `TargetEncoder.transform` verwenden, um die Kreuzvalidierung zu deaktivieren. Diese Kodierung wird dann an das Ridge-Modell übergeben. Führen Sie den folgenden Code aus, um das Ridge-Modell ohne Kreuzvalidierung zu trainieren:

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
