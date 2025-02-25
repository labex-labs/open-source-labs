# Trazar el gráfico

Ahora que tenemos nuestros datos de ejemplo, podemos trazar el gráfico utilizando la función `errorbar()`. Pasaremos las matrices `x` e `y` como los primeros dos parámetros. Luego, especificaremos el error en la dirección x como 0,2 y el error en la dirección y como 0,4 utilizando los parámetros `xerr` e `yerr`, respectivamente.

```python
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()
```
