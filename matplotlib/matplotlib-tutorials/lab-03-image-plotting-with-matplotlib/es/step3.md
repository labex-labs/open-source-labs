# Aplicando esquemas de pseudocolores

Los esquemas de pseudocolores se pueden utilizar para mejorar el contraste y visualizar los datos de manera más fácil. Si la imagen es en escala de grises, podemos aplicar esquemas de pseudocolores especificando diferentes mapas de colores. Esto se puede hacer utilizando el parámetro `cmap` en la función `imshow`.

```python
lum_img = img[:, :, 0]
plt.imshow(lum_img, cmap="hot")
```
