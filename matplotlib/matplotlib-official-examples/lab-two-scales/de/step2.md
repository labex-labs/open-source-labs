# Erstelle einige simulierte Daten

Als nächstes werden wir einige simulierte Daten erstellen, die wir für unsere Plots verwenden werden. Wir werden `numpy.arange` verwenden, um ein Array von Werten im Bereich von 0,01 bis 10,0 mit einem Schritt von 0,01 zu erstellen. Anschließend werden wir `numpy.exp` und `numpy.sin` verwenden, um zwei Datensätze zu erstellen.

```python
# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
```
