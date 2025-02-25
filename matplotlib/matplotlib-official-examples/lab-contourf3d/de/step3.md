# Generiere die Daten

Wir werden nun die Daten generieren, die für den 3D-Konturplot verwendet werden sollen. Wir werden die Methode `axes3d.get_test_data()` verwenden, um die Daten zu generieren. Diese Methode generiert Testdaten für einen 3D-Graphen.

```python
X, Y, Z = axes3d.get_test_data(0.05)
```
