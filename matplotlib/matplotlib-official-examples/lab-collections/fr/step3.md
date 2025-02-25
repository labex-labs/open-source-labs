# Créez des décalages

```python
# Fixing random state for reproducibility
rs = np.random.RandomState(19680801)

# Make some offsets
xyo = rs.randn(npts, 2)
```

La troisième étape est de créer des décalages à l'aide de Numpy. Nous utiliserons la fonction aléatoire pour créer les décalages.
