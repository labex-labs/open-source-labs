# Crear hélices

```python
nverts = 50
npts = 100

# Hacer algunas hélices
r = np.arange(nverts)
theta = np.linspace(0, 2*np.pi, nverts)
xx = r * np.sin(theta)
yy = r * np.cos(theta)
spiral = np.column_stack([xx, yy])
```

El siguiente paso es crear hélices utilizando Numpy. Utilizaremos las funciones seno y coseno para crear las hélices.
