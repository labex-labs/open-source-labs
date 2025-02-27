# Bewerte das Modell

Wir werden nun das trainierte Modell mit der Validierungsset bewerten. Die Bewertungsmetrik, die hier verwendet wird, ist der R-Quadrat-Wert.

```python
# Bewerte das Modell auf der Validierungsset
score = model.score(X_val, y_val)
print("Validierungsscore:", score)
```
