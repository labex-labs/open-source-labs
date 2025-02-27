# Leistung计算

Schließlich werden wir die Leistung des Klassifizierers durch Berechnung der Genauigkeit seiner Vorhersagen auf dem Testsatz evaluieren.

```python
accuracy = accuracy_score(y_test, y_pred)
print("Genauigkeit:", accuracy)
```