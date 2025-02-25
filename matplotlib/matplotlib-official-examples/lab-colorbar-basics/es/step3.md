# Crear un gráfico y una barra de color para datos positivos

Creamos un gráfico de los datos positivos y agregamos una barra de color al gráfico usando la función `colorbar`.

```python
# plot just the positive data and save the
# color "mappable" object returned by ax1.imshow
pos = plt.imshow(Zpos, cmap='Blues', interpolation='none')

# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which axes object it should be near
plt.colorbar(pos)
```
