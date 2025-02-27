# Vorhersage von Ausreißern

Sobald das Modell trainiert ist, können wir die `predict`-Methode verwenden, um vorherzusagen, ob neue Beobachtungen Ausreißer sind oder nicht. Die `predict`-Methode gibt 1 für Innenelemente und -1 für Ausreißer zurück.

```python
X_test = [5.5, 8.5]
predictions = estimator.predict(X_test)
print(predictions)
```
