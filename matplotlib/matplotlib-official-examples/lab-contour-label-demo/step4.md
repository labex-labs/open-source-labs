# Use a Formatter

We can also use a formatter to format the contour labels. This will allow us to format the labels in a specific way. In this example, we will use a `LogFormatterMathtext` to format the labels.

```python
fig2, ax2 = plt.subplots()
CS2 = ax2.contour(X, Y, 100**Z, locator=plt.LogLocator())
fmt = ticker.LogFormatterMathtext()
fmt.create_dummy_axis()
ax2.clabel(CS2, CS2.levels, fmt=fmt)
ax2.set_title("$100^Z$")

plt.show()
```
