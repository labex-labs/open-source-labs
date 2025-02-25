# Esquemas de interpolación de matrices

Al cambiar el tamaño de una imagen, es necesario interpolar los valores de los píxeles para llenar el espacio faltante. Se pueden utilizar diferentes esquemas de interpolación para determinar el valor de un píxel en función de sus píxeles circundantes. Matplotlib proporciona diferentes opciones de interpolación, como "nearest" (más cercano), "bilinear" (bilineal) y "bicubic" (bicúbica).

```python
plt.imshow(img, interpolation="bilinear")
```
