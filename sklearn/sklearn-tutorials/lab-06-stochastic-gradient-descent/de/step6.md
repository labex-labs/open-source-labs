# Vorhersagen treffen

Sobald der Klassifikator (classifier) trainiert ist, können wir ihn verwenden, um Vorhersagen für neue Daten zu treffen. Hier werden wir ihn nutzen, um die Zielklassen (target classes) für den Testsatz vorherzusagen.

```python
y_pred = clf.predict(X_test)
```
