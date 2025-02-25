# Utiliser un formateur

Nous pouvons également utiliser un formateur pour formater les étiquettes de contour. Cela nous permettra de formater les étiquettes d'une manière spécifique. Dans cet exemple, nous utiliserons un `LogFormatterMathtext` pour formater les étiquettes.

```python
fig2, ax2 = plt.subplots()
CS2 = ax2.contour(X, Y, 100**Z, locator=plt.LogLocator())
fmt = ticker.LogFormatterMathtext()
fmt.create_dummy_axis()
ax2.clabel(CS2, CS2.levels, fmt=fmt)
ax2.set_title("$100^Z$")

plt.show()
```
