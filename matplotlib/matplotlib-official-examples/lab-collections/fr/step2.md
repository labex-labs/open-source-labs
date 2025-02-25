# Créez des spirales

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

L'étape suivante est de créer des spirales à l'aide de Numpy. Nous utiliserons les fonctions sin et cos pour créer les spirales.
