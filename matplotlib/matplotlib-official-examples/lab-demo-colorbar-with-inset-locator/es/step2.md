# Crear un gráfico e imagen

A continuación, crearemos un gráfico e una imagen para mostrar cómo agregar una barra de color utilizando ejes insertados.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[6, 3])

im1 = ax1.imshow([[1, 2], [2, 3]])
im2 = ax2.imshow([[1, 2], [2, 3]])
```
