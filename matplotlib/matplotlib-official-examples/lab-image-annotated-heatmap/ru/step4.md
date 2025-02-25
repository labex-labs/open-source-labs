# Более сложные примеры тепловых карточек

В следующем разделе мы демонстрируем гибкость ранее созданных функций, применяя их в различных случаях и используя разные аргументы.

```python
np.random.seed(19680801)

fig, ((ax, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 6))

# Повторите вышеприведенный пример с другим размером шрифта и цветовой картой.

im, _ = heatmap(harvest, vegetables, farmers, ax=ax, cmap="Wistia", cbarlabel="harvest [t/year]")
annotate_heatmap(im, valfmt="{x:.1f}", size=7)

# Иногда даже сами данные являются категориальными. Здесь мы используем `matplotlib.colors.BoundaryNorm`, чтобы разделить данные на классы и использовать это для цветовой кодировки графика, а также для получения меток классов из массива классов.

data = np.random.randn(6, 6)
y = [f"Prod. {i}" for i in range(10, 70, 10)]
x = [f"Cycle {i}" for i in range(1, 7)]

qrates = list("ABCDEFG")
norm = matplotlib.colors.BoundaryNorm(np.linspace(-3.5, 3.5, 8), 7)
fmt = matplotlib.ticker.FuncFormatter(lambda x, pos: qrates[::-1][norm(x)])

im, _ = heatmap(data, y, x, ax=ax3, cmap=mpl.colormaps["PiYG"].resampled(7), norm=norm, cbar_kw=dict(ticks=np.arange(-3, 4), format=fmt), cbarlabel="Quality Rating")
annotate_heatmap(im, valfmt=fmt, size=9, fontweight="bold", threshold=-1, textcolors=("red", "black"))

# Мы можем красиво нарисовать матрицу корреляции. Поскольку она ограничена значениями от -1 до 1, мы используем эти значения в качестве vmin и vmax.

corr_matrix = np.corrcoef(harvest)
im, _ = heatmap(corr_matrix, vegetables, vegetables, ax=ax4, cmap="PuOr", vmin=-1, vmax=1, cbarlabel="correlation coeff.")
annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)

plt.tight_layout()
plt.show()
```
