# Den Random Forest-Klassifizierer bewerten

Lassen Sie uns den Random Forest-Klassifizierer bewerten, indem wir die Genauigkeit auf den Testdaten berechnen.

```python
accuracy = random_forest.score(X_test, y_test)
print(f"Genauigkeit des Random Forest-Klassifizierers: {accuracy}")
```