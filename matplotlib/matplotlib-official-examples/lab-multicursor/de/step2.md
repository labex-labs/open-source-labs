# Daten erstellen

Als nächstes werden wir einige Daten für unsere Diagramme erstellen. In diesem Beispiel werden wir drei Sinuswellen mit unterschiedlichen Frequenzen erstellen.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(3*np.pi*t)
s3 = np.sin(4*np.pi*t)
```
