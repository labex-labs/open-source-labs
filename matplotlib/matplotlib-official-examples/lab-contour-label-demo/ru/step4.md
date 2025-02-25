# Использование Форматировщика

Мы также можем использовать форматтер для форматирования контурных подписей. Это позволит нам форматировать подписи определенным образом. В этом примере мы будем использовать `LogFormatterMathtext` для форматирования подписей.

```python
fig2, ax2 = plt.subplots()
CS2 = ax2.contour(X, Y, 100**Z, locator=plt.LogLocator())
fmt = ticker.LogFormatterMathtext()
fmt.create_dummy_axis()
ax2.clabel(CS2, CS2.levels, fmt=fmt)
ax2.set_title("$100^Z$")

plt.show()
```
