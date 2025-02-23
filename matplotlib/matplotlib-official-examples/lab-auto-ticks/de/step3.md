# Streudiagramm mit zusätzlichem Rand

In diesem Schritt werden wir einen zusätzlichen Rand um die Daten festlegen, indem wir `.Axes.set_xmargin` / `.Axes.set_ymargin` verwenden, wobei das autolimit_mode mit geraden Zahlen weiterhin beachtet wird.

```python
fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
ax.set_xmargin(0.8)
plt.show()
```
