# Vorhersagen und Genauigkeit messen

Wir prognostizieren die Klassenbezeichnungen für die Eingabedaten und messen die Genauigkeit des Klassifiziers.

```python
y_pred = clf.predict(X)
print("Accuracy: ", np.mean(y == y_pred))
```
