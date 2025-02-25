# Bilder aktualisieren

Schließlich werden wir die Bilder aktualisieren, um auf Änderungen in der Norm anderer Bilder zu reagieren. Dies wird es uns ermöglichen, die Farbskala und die Farbpalette eines Bilds zu ändern und alle anderen entsprechend zu aktualisieren.

```python
def update(changed_image):
    for im in images:
        if (changed_image.get_cmap()!= im.get_cmap()
                or changed_image.get_clim()!= im.get_clim()):
            im.set_cmap(changed_image.get_cmap())
            im.set_clim(changed_image.get_clim())

for im in images:
    im.callbacks.connect('changed', update)
```
