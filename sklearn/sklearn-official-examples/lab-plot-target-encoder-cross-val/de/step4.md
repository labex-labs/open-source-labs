# Training eines Ridge-Regressors auf Rohdaten

In diesem Abschnitt werden wir einen Ridge-Regressor auf dem Datensatz mit und ohne Kodierung trainieren und den Einfluss des Zielkodierers (Target Encoder) mit und ohne Intervall-Kreuzvalidierung untersuchen. Zunächst werden wir ein Ridge-Modell auf den Rohmerkmalen trainieren. Führen Sie den folgenden Code aus, um das Ridge-Modell zu trainieren:

```python
ridge = Ridge(alpha=1e-6, solver="lsqr", fit_intercept=False)

raw_model = ridge.fit(X_train, y_train)
print("Raw Model score on training set: ", raw_model.score(X_train, y_train))
print("Raw Model score on test set: ", raw_model.score(X_test, y_test))
```
