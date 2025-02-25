# Figur und Teilplots erstellen

Der zweite Schritt besteht darin, die Figur und die Teilplots zu erstellen, die für die Animation verwendet werden sollen. In diesem Beispiel erstellen wir zwei nebeneinander liegende Teilplots mit unterschiedlichen Seitenverhältnissen. Der linke Teilplot ist ein Einingelkreis, und der rechte Teilplot ist ein leerer Plot, der zur Animation einer Sinuskurve verwendet werden soll.

```python
fig, (axl, axr) = plt.subplots(
    ncols=2,
    sharey=True,
    figsize=(6, 2),
    gridspec_kw=dict(width_ratios=[1, 3], wspace=0),
)
axl.set_aspect(1)
axr.set_box_aspect(1 / 3)
axr.yaxis.set_visible(False)
axr.xaxis.set_ticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])
```
