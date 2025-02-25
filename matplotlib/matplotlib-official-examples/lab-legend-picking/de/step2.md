# Daten vorbereiten

Wir werden mit NumPy zwei Sinuswellen mit unterschiedlichen Frequenzen erzeugen.

```python
t = np.linspace(0, 1)
y1 = 2 * np.sin(2*np.pi*t)
y2 = 4 * np.sin(2*np.pi*2*t)
```
