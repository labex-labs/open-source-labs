# Daten erstellen

Als nächstes werden wir die Daten für das Diagramm erstellen. Wir werden eine Sinuswelle mit der Bibliothek `numpy` erstellen.

```python
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
```
