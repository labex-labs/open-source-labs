# Iterar sobre la cuadrícula y graficar las imágenes

Luego, iteramos sobre el objeto `grid` usando la función `zip` para iterar tanto sobre los ejes como sobre las matrices de imágenes. Graficamos cada imagen en su eje correspondiente usando la función `imshow`.

```python
for ax, im in zip(grid, [im1, im2, im3, im4]):
    ax.imshow(im)
```
