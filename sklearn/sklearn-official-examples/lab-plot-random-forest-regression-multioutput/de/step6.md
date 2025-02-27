# Vorhersagen für neue Daten

Wir werden sowohl den Random Forest Regressor als auch den Multi-Output Regressor verwenden, um Vorhersagen für unsere Testdaten zu machen.

```python
y_rf = regr_rf.predict(X_test)
y_multirf = regr_multirf.predict(X_test)
```
