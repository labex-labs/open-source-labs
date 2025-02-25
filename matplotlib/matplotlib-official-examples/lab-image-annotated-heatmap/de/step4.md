# Komplexere Heatmap-Beispiele

Im Folgenden zeigen wir die Vielseitigkeit der zuvor erstellten Funktionen, indem wir sie in verschiedenen Fällen anwenden und verschiedene Argumente verwenden.

```python
np.random.seed(19680801)

fig, ((ax, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 6))

# Wiederhole das obige Beispiel mit einer anderen Schriftgröße und Farbpalette.

im, _ = heatmap(ernte, gemüsesorten, bauer, ax=ax, cmap="Wistia", cbarlabel="Ernte [t/Jahr]")
annotate_heatmap(im, valfmt="{x:.1f}", size=7)

# Manchmal ist sogar die Daten selbst kategorisch. Hier verwenden wir eine `matplotlib.colors.BoundaryNorm`, um die Daten in Klassen zu bringen und diese zur Färbung des Diagramms zu verwenden, aber auch, um die Klassenbezeichnungen aus einem Array von Klassen zu erhalten.

data = np.random.randn(6, 6)
y = [f"Prod. {i}" for i in range(10, 70, 10)]
x = [f"Cycle {i}" for i in range(1, 7)]

qrates = list("ABCDEFG")
norm = matplotlib.colors.BoundaryNorm(np.linspace(-3.5, 3.5, 8), 7)
fmt = matplotlib.ticker.FuncFormatter(lambda x, pos: qrates[::-1][norm(x)])

im, _ = heatmap(data, y, x, ax=ax3, cmap=mpl.colormaps["PiYG"].resampled(7), norm=norm, cbar_kw=dict(ticks=np.arange(-3, 4), format=fmt), cbarlabel="Quality Rating")
annotate_heatmap(im, valfmt=fmt, size=9, fontweight="bold", threshold=-1, textcolors=("red", "black"))

# Wir können eine Korrelationsmatrix schön plotten. Da diese zwischen -1 und 1 begrenzt ist, verwenden wir diese als vmin und vmax.

corr_matrix = np.corrcoef(ernte)
im, _ = heatmap(corr_matrix, gemüsesorten, gemüsesorten, ax=ax4, cmap="PuOr", vmin=-1, vmax=1, cbarlabel="Korrelationskoeffizient")
annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)

plt.tight_layout()
plt.show()
```
