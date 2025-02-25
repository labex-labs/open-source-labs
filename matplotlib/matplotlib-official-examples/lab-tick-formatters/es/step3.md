# Formateo de objetos Formatter

En este paso, usaremos objetos `.Formatter` para formatear las marcas. Crearemos siete gráficas, cada una usando un formateador diferente.

```python
fig1, axs1 = plt.subplots(7, 1, figsize=(8, 6))
fig1.suptitle('Formateo de objetos Formatter')

# Formateador nulo
setup(axs1[0], título="NullFormatter()")
axs1[0].xaxis.set_major_formatter(ticker.NullFormatter())

# Formateador StrMethod
setup(axs1[1], título="StrMethodFormatter('{x:.3f}')")
axs1[1].xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.3f}"))

# FuncFormatter se puede usar como decorador
@ticker.FuncFormatter
def major_formatter(x, pos):
    return f'[{x:.2f}]'

setup(axs1[2], título='FuncFormatter("[{:.2f}]".format)')
axs1[2].xaxis.set_major_formatter(major_formatter)

# Formateador fijo
setup(axs1[3], título="FixedFormatter(['A', 'B', 'C',...])")
# FixedFormatter solo debe usarse en conjunto con FixedLocator.
# De lo contrario, no se puede estar seguro de dónde terminarán las etiquetas.
positions = [0, 1, 2, 3, 4, 5]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
axs1[3].xaxis.set_major_locator(ticker.FixedLocator(posiciones))
axs1[3].xaxis.set_major_formatter(ticker.FixedFormatter(labels))

# Formateador escalar
setup(axs1[4], título="ScalarFormatter()")
axs1[4].xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))

# Formateador FormatStr
setup(axs1[5], título="FormatStrFormatter('#%d')")
axs1[5].xaxis.set_major_formatter(ticker.FormatStrFormatter("#%d"))

# Formateador porcentual
setup(axs1[6], título="PercentFormatter(xmax=5)")
axs1[6].xaxis.set_major_formatter(ticker.PercentFormatter(xmax=5))

fig1.tight_layout()
```
