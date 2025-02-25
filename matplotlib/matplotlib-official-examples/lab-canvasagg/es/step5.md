# Guardar la matriz de numpy en una imagen de Pillow

Ahora que tenemos la matriz de numpy, podemos pasarla a Pillow y guardarla en cualquier formato admitido por Pillow. En este ejemplo, guardaremos la trama como una imagen BMP.

```python
im = Image.fromarray(rgba)
im.save("test.bmp")
```
