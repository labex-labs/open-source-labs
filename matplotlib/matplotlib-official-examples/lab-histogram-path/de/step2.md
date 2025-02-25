# Setzen des Zufallszufalls und Generieren von Daten

Wir werden numpy verwenden, um zufällige Daten zu generieren. Um unsere Ergebnisse reproduzierbar zu machen, werden wir einen Zufallszufall setzen. Fügen Sie den folgenden Code zu Ihrer Datei hinzu:

```python
np.random.seed(19680801)
data = np.random.randn(1000)
```
