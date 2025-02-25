# Spiralen erstellen

```python
nverts = 50
npts = 100

# Make some spirals
r = np.arange(nverts)
theta = np.linspace(0, 2*np.pi, nverts)
xx = r * np.sin(theta)
yy = r * np.cos(theta)
spiral = np.column_stack([xx, yy])
```

Als nächster Schritt erstellen wir Spiralen mit Numpy. Wir werden die sin- und cos-Funktionen verwenden, um die Spiralen zu erstellen.
