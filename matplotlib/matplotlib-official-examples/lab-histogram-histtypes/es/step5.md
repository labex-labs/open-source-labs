# Cambiar el estilo del histograma

Podemos cambiar el estilo del histograma especificando el parámetro `histtype` en la función `hist`. En este ejemplo, crearemos un histograma con una curva de escalón que tiene un relleno de color.

```python
plt.hist(x, bins=20, density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.show()
```
