# Erzeugen von Häckmuster mit nicht belegter Farbe

Wir können Häckmuster mit nicht belegter Farbe erzeugen, indem wir den Parameter `colors` in `ax.tricontourf` als `"none"` angeben. Wir können auch eine Legende für den Kontursatz mit `ContourSet.legend_elements` erstellen.

```python
fig3, ax3 = plt.subplots()
n_levels = 7
tcf = ax3.tricontourf(
    triang,
    z,
    n_levels,
    colors="none",
    hatches=[".", "/", "\\", None, "\\\\", "*"],
)
ax3.tricontour(triang, z, n_levels, colors="black", linestyles="-")

artists, labels = tcf.legend_elements(str_format="{:2.1f}".format)
ax3.legend(artists, labels, handleheight=2, framealpha=1)
```
