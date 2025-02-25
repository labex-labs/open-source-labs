# Farbskala einstellen und Farbskala erstellen

Jetzt werden wir die Farbskala für unsere Bilder einstellen und eine Farbskala erstellen, um den Wertebereich anzuzeigen. Wir werden den kleinsten und größten Wert für alle Bilder finden und die Farbskala entsprechend normalisieren.

```python
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axs, orientation='horizontal', fraction=.1)
```
