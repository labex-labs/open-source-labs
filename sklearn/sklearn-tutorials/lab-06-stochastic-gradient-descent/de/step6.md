# Vorhersagen treffen

Sobald der Klassifizierer trainiert ist, können wir ihn verwenden, um Vorhersagen für neue Daten zu treffen. Hier werden wir ihn verwenden, um die Zielklassen für den Testsatz vorherzusagen.

```python
y_pred = clf.predict(X_test)
```