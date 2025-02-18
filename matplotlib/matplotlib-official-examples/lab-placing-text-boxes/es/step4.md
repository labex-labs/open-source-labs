# Crear texto para el cuadro de texto

Crearemos una cadena que contenga la media, la mediana y la desviación estándar de nuestros datos.

```python
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu, ),
    r'$\mathrm{median}=%.2f$' % (median, ),
    r'$\sigma=%.2f$' % (sigma, )))
```
