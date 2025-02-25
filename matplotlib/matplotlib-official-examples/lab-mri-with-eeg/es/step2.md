# Graficar el histograma de la intensidad de la resonancia magnética

A continuación, graficaremos el histograma de la intensidad de la resonancia magnética utilizando la función `hist()`. Normalizaremos los valores de intensidad para que estén en el rango entre 0 y 1.

```python
# Graficar el histograma de la intensidad de la resonancia magnética
ax1 = fig.add_subplot(2, 2, 2)
im = np.ravel(im)
im = im[np.nonzero(im)]  # Ignorar el fondo
im = im / im.max()  # Normalizar
ax1.hist(im, bins=100)
ax1.set_xlabel('Intensidad (a.u.)')
ax1.set_ylabel('Densidad de resonancia magnética')
```
