# Vorhersagen

In diesem Schritt werden wir Vorhersagen mit den Modellen machen, die wir im vorherigen Schritt erstellt haben. Wir werden `np.arange` verwenden, um ein neues Array von Werten von -100 bis 100 mit einem Intervall von 0,01 zu erstellen, und anschließend werden wir die `predict`-Methode unserer Modelle verwenden, um die Ausgabe vorherzusagen.

```python
# Predict
X_test = np.arange(-100.0, 100.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
y_3 = regr_3.predict(X_test)
```
