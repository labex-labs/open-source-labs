# Daten erstellen

Als nächster Schritt müssen wir die Daten für die 3D-Oberfläche erstellen. Dazu definieren wir `u`, `v`, `x`, `y` und `z`. Diese Variablen werden die Winkel und Koordinaten repräsentieren, die zur Darstellung der Oberfläche erforderlich sind. Die `linspace()`-Funktion aus NumPy wird verwendet, um die Winkel zu erstellen, und die `outer()`-Funktion wird verwendet, um die Koordinaten zu erstellen.

```python
# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
```
