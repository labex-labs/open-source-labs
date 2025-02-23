# Quadratisches Verknüpfungs-/Randdiagramm

Es kann wünschenswert sein, neben einem Diagramm von Verknüpfungsdaten die Randverteilungen anzuzeigen. Folgender Code erstellt ein quadratisches Diagramm, bei dem das Seitenverhältnis der Randachsen gleich dem Verhältnis der Breite und Höhe des `gridspec` ist. Dies gewährleistet, dass alle Achsen perfekt ausgerichtet sind, unabhängig von der Größe der Figur.

```python
fig5, axs = plt.subplots(2, 2, sharex="col", sharey="row",
                         gridspec_kw=dict(height_ratios=[1, 3],
                                          width_ratios=[3, 1]))
axs[0, 1].set_visible(False)
axs[0, 0].set_box_aspect(1/3)
axs[1, 0].set_box_aspect(1)
axs[1, 1].set_box_aspect(3/1)

np.random.seed(19680801)  # Fixing random state for reproducibility
x, y = np.random.randn(2, 400) * [[.5], [180]]
axs[1, 0].scatter(x, y)
axs[0, 0].hist(x)
axs[1, 1].hist(y, orientation="horizontal")

plt.show()
```
