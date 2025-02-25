# Daten generieren

Wir generieren einige Beispiel-Daten, die geplottet werden sollen. Hier verwenden wir die `numpy`-Bibliothek, um drei Datenarrays zu generieren.

```python
t = np.arange(0.0, 2.0, 0.01)

s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = s1 * s2
```
