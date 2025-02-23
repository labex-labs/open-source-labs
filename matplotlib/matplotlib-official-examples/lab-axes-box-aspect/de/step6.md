# Seitenverhältnis für viele Teilplots

Es ist möglich, das Seitenverhältnis an eine Achse beim Initialisieren zu übergeben. Folgender Code erstellt ein 2x3 Teilplot-Gitter mit allen quadratischen Achsen.

```python
fig7, axs = plt.subplots(2, 3, subplot_kw=dict(box_aspect=1),
                         sharex=True, sharey=True, layout="constrained")

for i, ax in enumerate(axs.flat):
    ax.scatter(i % 3, -((i // 3) - 0.5)*200, c=[plt.cm.hsv(i / 6)], s=300)
plt.show()
```
