# Utiliza un Formateador

También podemos utilizar un formateador para formatear las etiquetas de contorno. Esto nos permitirá formatear las etiquetas de una manera específica. En este ejemplo, usaremos un `LogFormatterMathtext` para formatear las etiquetas.

```python
fig2, ax2 = plt.subplots()
CS2 = ax2.contour(X, Y, 100**Z, locator=plt.LogLocator())
fmt = ticker.LogFormatterMathtext()
fmt.create_dummy_axis()
ax2.clabel(CS2, CS2.levels, fmt=fmt)
ax2.set_title("$100^Z$")

plt.show()
```
