# Daten erstellen

Als nächstes werden wir die Daten erstellen, die im Diagramm verwendet werden sollen. Mit der `numpy`-Bibliothek werden wir drei unterschiedliche Sinuswellen mit unterschiedlichen Frequenzen erstellen.

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)
```
