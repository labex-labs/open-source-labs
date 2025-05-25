# Criar espirais

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

O próximo passo é criar espirais usando Numpy. Usaremos as funções sin e cos para criar as espirais.
