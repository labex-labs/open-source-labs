# Verwenden eines Formatters

Wir können auch einen Formatter verwenden, um die Konturbeschriftungen zu formatieren. Dies wird uns ermöglichen, die Beschriftungen auf eine bestimmte Weise zu formatieren. In diesem Beispiel werden wir einen `LogFormatterMathtext` verwenden, um die Beschriftungen zu formatieren.

```python
fig2, ax2 = plt.subplots()
CS2 = ax2.contour(X, Y, 100**Z, locator=plt.LogLocator())
fmt = ticker.LogFormatterMathtext()
fmt.create_dummy_axis()
ax2.clabel(CS2, CS2.levels, fmt=fmt)
ax2.set_title("$100^Z$")

plt.show()
```
