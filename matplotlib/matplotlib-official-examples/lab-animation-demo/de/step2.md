# Zufällige Daten generieren

Wir werden eine 3D-Array von Zufallsdaten mit `numpy.random.random()` generieren. Wir werden einen Seed-Wert verwenden, um sicherzustellen, dass die gleiche Menge an Daten jedes Mal generiert wird, wenn der Code ausgeführt wird.

```python
np.random.seed(19680801)
data = np.random.random((50, 50, 50))
```
