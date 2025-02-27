# Bewertung des Modells

Um die Leistung unseres Modells zu bewerten, können wir die `accuracy_score`-Funktion von scikit-learn verwenden:

```python
from sklearn.metrics import accuracy_score

# Vorhersagen der Labels des Testsets
y_pred = clf.predict(X_test)

# Berechnung der Genauigkeit des Modells
accuracy = accuracy_score(y_test, y_pred)

# Ausgabe der Genauigkeit des Modells
print("Genauigkeit:", accuracy)
```
