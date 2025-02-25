# Crear una gráfica

A continuación, crearemos una gráfica simple utilizando NumPy. Esta gráfica servirá como fondo para las flechas de dirección ancladas.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))
```
