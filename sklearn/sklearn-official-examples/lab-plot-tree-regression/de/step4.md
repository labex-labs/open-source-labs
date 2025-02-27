# Vorhersagen

Wir werden die Modelle verwenden, um Vorhersagen für einen Wertebereich von 0 bis 5 zu treffen.

```python
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
```
