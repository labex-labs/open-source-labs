# Formatage d'objets Formatter

Dans cette étape, nous allons utiliser des objets `.Formatter` pour formater les étiquettes. Nous allons créer sept tracés, chacun utilisant un formatteur différent.

```python
fig1, axs1 = plt.subplots(7, 1, figsize=(8, 6))
fig1.suptitle('Formatage d\'objets Formatter')

# Formatteur nul
setup(axs1[0], titre="NullFormatter()")
axs1[0].xaxis.set_major_formatter(ticker.NullFormatter())

# Formatteur StrMethod
setup(axs1[1], titre="StrMethodFormatter('{x:.3f}')")
axs1[1].xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.3f}"))

# FuncFormatter peut être utilisé comme décorateur
@ticker.FuncFormatter
def major_formatter(x, pos):
    return f'[{x:.2f}]'

setup(axs1[2], titre='FuncFormatter("[{:.2f}]".format)')
axs1[2].xaxis.set_major_formatter(major_formatter)

# Formatteur fixe
setup(axs1[3], titre="FixedFormatter(['A', 'B', 'C',...])")
# FixedFormatter ne devrait être utilisé que conjointement avec FixedLocator.
# Sinon, on ne peut pas être sûr où les étiquettes finiront.
positions = [0, 1, 2, 3, 4, 5]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
axs1[3].xaxis.set_major_locator(ticker.FixedLocator(positions))
axs1[3].xaxis.set_major_formatter(ticker.FixedFormatter(labels))

# Formatteur scalaire
setup(axs1[4], titre="ScalarFormatter()")
axs1[4].xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))

# Formatteur FormatStr
setup(axs1[5], titre="FormatStrFormatter('#%d')")
axs1[5].xaxis.set_major_formatter(ticker.FormatStrFormatter("#%d"))

# Formatteur pourcentage
setup(axs1[6], titre="PercentFormatter(xmax=5)")
axs1[6].xaxis.set_major_formatter(ticker.PercentFormatter(xmax=5))

fig1.tight_layout()
```
