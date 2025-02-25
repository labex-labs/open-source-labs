# Erstellen des 3D-Gitterplots

Wir werden für das zweite Teilbild einen 3D-Gitterplot erstellen. Wir werden die Funktion `get_test_data` aus mpl_toolkits.mplot3d.axes3d verwenden, um die Daten für den Plot zu erstellen.

```python
# Create data for the 3D wireframe plot
X, Y, Z = Axes3D.get_test_data(0.05)

# Plot the 3D wireframe plot
ax2.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
