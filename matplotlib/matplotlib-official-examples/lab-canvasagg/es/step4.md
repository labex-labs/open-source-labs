# Extraer el búfer del renderizador a una matriz de numpy

La segunda opción para guardar la trama es extraer el búfer del renderizador a una matriz de numpy. Esto nos permite utilizar Matplotlib dentro de un script cgi sin necesidad de escribir una figura en el disco. En este ejemplo, extraeremos el búfer del renderizador y lo convertiremos en una matriz de numpy.

```python
canvas.draw()
rgba = np.asarray(canvas.buffer_rgba())
```
