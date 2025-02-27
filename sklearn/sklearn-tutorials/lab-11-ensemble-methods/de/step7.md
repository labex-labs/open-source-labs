# Bewertung des Random Forest-Klassifikators

Lassen Sie uns den Random Forest-Klassifikator bewerten, indem wir die Genauigkeit (Accuracy) auf den Testdaten berechnen.

```python
accuracy = random_forest.score(X_test, y_test)
print(f"Random Forest Classifier Accuracy: {accuracy}")
```
