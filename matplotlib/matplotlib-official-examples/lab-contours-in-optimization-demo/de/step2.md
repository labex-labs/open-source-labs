# Einrichten der Messvektoren und -matrizen

Als nächstes richten Sie die Messvektoren und -matrizen ein. Entwerfen Sie die Scheibenbelastung und das Übersetzungsverhältnis.

```python
nx = 101
ny = 105

# Set up survey vectors
xvec = np.linspace(0.001, 4.0, nx)
yvec = np.linspace(0.001, 4.0, ny)

# Set up survey matrices.  Design disk loading and gear ratio.
x1, x2 = np.meshgrid(xvec, yvec)
```
