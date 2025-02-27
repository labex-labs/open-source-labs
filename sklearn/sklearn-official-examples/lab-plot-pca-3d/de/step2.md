# Daten erstellen

Wir werden für dieses Lab ein zufälliges Datenset generieren. Das Datenset wird drei Variablen `x`, `y` und `z` haben. Wir werden `x` und `y` als normalverteilte Zufallsvariablen mit Mittelwert 0 und Standardabweichung von 0,5 definieren. `z` ist ebenfalls normalverteilt mit Mittelwert 0 und Standardabweichung von 0,1.

```python
e = np.exp(1)
np.random.seed(4)

y = np.random.normal(scale=0.5, size=(30000))
x = np.random.normal(scale=0.5, size=(30000))
z = np.random.normal(scale=0.1, size=len(x))
```
