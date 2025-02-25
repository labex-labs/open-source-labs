# Crear una imagen con un enlace hipervinculo

En este paso, crearemos una imagen y le agregaremos un enlace hipervinculo. Aquí está el código para crear la imagen:

```python
fig = plt.figure()
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.gray,
                origin='lower', extent=[-3, 3, -3, 3])
```

Para agregar un enlace hipervinculo a la imagen, debemos utilizar el método `set_url()` del objeto de la imagen. Este método toma una URL como argumento. Aquí está el código actualizado:

```python
im.set_url('https://www.google.com/')
```

La imagen tendrá un enlace hipervinculo a `https://www.google.com/`. Finalmente, podemos guardar el gráfico como un archivo SVG utilizando `fig.savefig()`:

```python
fig.savefig('image.svg')
```
