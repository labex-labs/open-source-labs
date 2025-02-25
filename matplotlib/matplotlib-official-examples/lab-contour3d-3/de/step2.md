# Erstellen einer 3D-Grafik und Daten

In diesem Schritt erstellen wir eine 3D-Grafik und erhalten Testdaten für den Oberflächenplot.

```python
# Erstellen einer 3D-Grafik
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Erhalten von Testdaten für den Oberflächenplot
X, Y, Z = axes3d.get_test_data(0.05)
```
