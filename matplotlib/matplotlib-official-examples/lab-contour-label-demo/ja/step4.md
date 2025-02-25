# フォーマッタを使用する

等高線ラベルをフォーマットするために、フォーマッタを使用することもできます。これにより、特定の方法でラベルをフォーマットすることができます。この例では、`LogFormatterMathtext` を使用してラベルをフォーマットします。

```python
fig2, ax2 = plt.subplots()
CS2 = ax2.contour(X, Y, 100**Z, locator=plt.LogLocator())
fmt = ticker.LogFormatterMathtext()
fmt.create_dummy_axis()
ax2.clabel(CS2, CS2.levels, fmt=fmt)
ax2.set_title("$100^Z$")

plt.show()
```
