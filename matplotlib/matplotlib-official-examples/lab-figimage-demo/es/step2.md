# Creando la figura y la imagen

A continuación, creamos la figura y la imagen que queremos colocar en ella. En este ejemplo, creamos una matriz de 100x100 de valores aleatorios y establecemos los valores en la mitad derecha de la imagen en 1. Luego creamos dos instancias separadas de la imagen, cada una con una posición y opacidad diferentes.

```python
fig = plt.figure()
Z = np.arange(10000).reshape((100, 100))
Z[:, 50:] = 1

im1 = fig.figimage(Z, xo=50, yo=0, origin='lower')
im2 = fig.figimage(Z, xo=100, yo=100, alpha=.8, origin='lower')
```
