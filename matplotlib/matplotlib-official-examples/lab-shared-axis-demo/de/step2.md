# Daten für die Diagramme erstellen

Wir müssen Daten für die Diagramme erstellen, um sie zu visualisieren. In diesem Beispiel werden wir drei verschiedene Datensätze mit NumPy erstellen.

```python
t = np.arange(0.01, 5.0, 0.01)
s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = np.sin(4 * np.pi * t)
```
