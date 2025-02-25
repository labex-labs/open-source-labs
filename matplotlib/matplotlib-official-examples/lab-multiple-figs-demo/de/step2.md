# Erstelle Daten

Als nächstes müssen wir einige Daten erstellen, um sie zu plotten. Wir werden zwei Sinuswellen erstellen, die wir in separaten Diagrammen plotten werden.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)
```
