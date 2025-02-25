# Combinar transparencia

La forma más simple de incluir transparencia al graficar datos con `imshow` es pasar una matriz con la misma forma que los datos al argumento `alpha`.

```python
# Crear una canal alfa con valores que aumentan linealmente hacia la derecha.
alphas = np.ones(weights.shape)
alphas[:, 30:] = np.linspace(1, 0, 70)

# Crear la figura y la imagen
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)
ax.set_axis_off()
plt.show()
```
