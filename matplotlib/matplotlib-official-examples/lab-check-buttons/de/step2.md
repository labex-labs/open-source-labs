# Daten generieren

Als nächstes werden wir die Daten für unseren Plot generieren. Wir werden mit `numpy` drei Sinuswellen mit unterschiedlichen Frequenzen erstellen.

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(6*np.pi*t)
```
