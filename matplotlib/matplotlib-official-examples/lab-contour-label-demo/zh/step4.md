# 使用格式化器

我们还可以使用格式化器来格式化等高线标签。这将使我们能够以特定方式格式化标签。在这个例子中，我们将使用`LogFormatterMathtext`来格式化标签。

```python
fig2, ax2 = plt.subplots()
CS2 = ax2.contour(X, Y, 100**Z, locator=plt.LogLocator())
fmt = ticker.LogFormatterMathtext()
fmt.create_dummy_axis()
ax2.clabel(CS2, CS2.levels, fmt=fmt)
ax2.set_title("$100^Z$")

plt.show()
```
