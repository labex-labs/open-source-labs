# Usando um Formatter

Também podemos usar um _formatter_ (formatador) para formatar os rótulos de contorno. Isso nos permitirá formatar os rótulos de uma maneira específica. Neste exemplo, usaremos um `LogFormatterMathtext` para formatar os rótulos.

```python
fig2, ax2 = plt.subplots()
CS2 = ax2.contour(X, Y, 100**Z, locator=plt.LogLocator())
fmt = ticker.LogFormatterMathtext()
fmt.create_dummy_axis()
ax2.clabel(CS2, CS2.levels, fmt=fmt)
ax2.set_title("$100^Z$")

plt.show()
```
