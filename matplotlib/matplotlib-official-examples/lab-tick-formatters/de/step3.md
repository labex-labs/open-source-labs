# Formatierung von Formatter-Objekten

In diesem Schritt werden wir `.Formatter`-Objekte verwenden, um die Tick-Markierungen zu formatieren. Wir werden sieben Graphen erstellen, wobei jeder einen anderen Formatter verwendet.

```python
fig1, axs1 = plt.subplots(7, 1, figsize=(8, 6))
fig1.suptitle('Formatter Object Formatting')

# Null-Formatter
setup(axs1[0], title="NullFormatter()")
axs1[0].xaxis.set_major_formatter(ticker.NullFormatter())

# StrMethod-Formatter
setup(axs1[1], title="StrMethodFormatter('{x:.3f}')")
axs1[1].xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.3f}"))

# FuncFormatter kann als Dekorator verwendet werden
@ticker.FuncFormatter
def major_formatter(x, pos):
    return f'[{x:.2f}]'

setup(axs1[2], title='FuncFormatter("[{:.2f}]".format)')
axs1[2].xaxis.set_major_formatter(major_formatter)

# Fixed-Formatter
setup(axs1[3], title="FixedFormatter(['A', 'B', 'C',...])")
# FixedFormatter sollte nur zusammen mit FixedLocator verwendet werden.
# Andernfalls kann man nicht sicher sein, wo die Labels landen werden.
positions = [0, 1, 2, 3, 4, 5]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
axs1[3].xaxis.set_major_locator(ticker.FixedLocator(positions))
axs1[3].xaxis.set_major_formatter(ticker.FixedFormatter(labels))

# Scalar-Formatter
setup(axs1[4], title="ScalarFormatter()")
axs1[4].xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))

# FormatStr-Formatter
setup(axs1[5], title="FormatStrFormatter('#%d')")
axs1[5].xaxis.set_major_formatter(ticker.FormatStrFormatter("#%d"))

# Prozent-Formatter
setup(axs1[6], title="PercentFormatter(xmax=5)")
axs1[6].xaxis.set_major_formatter(ticker.PercentFormatter(xmax=5))

fig1.tight_layout()
```
