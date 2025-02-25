# Crear gráficos

A continuación, creemos dos gráficos utilizando `imshow` y matrices aleatorias generadas por `numpy.random`. También agregaremos una barra de colores a los gráficos. Ejecute el siguiente código:

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

plt.subplot(211)
plt.imshow(np.random.random((100, 100)))
plt.subplot(212)
plt.imshow(np.random.random((100, 100)))

cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)

plt.show()
```
