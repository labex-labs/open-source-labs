# Vorschaubilder generieren

In diesem Schritt generieren Sie Vorschaubilder für alle Bilder im angegebenen Verzeichnis. Sie verwenden eine for-Schleife, um über alle Bilder mit der `.png`-Erweiterung im angegebenen Verzeichnis zu iterieren. Für jedes Bild generieren Sie ein Vorschaubild und speichern es im `thumbs`-Verzeichnis.

```python
for path in args.imagedir.glob("*.png"):
    outpath = outdir / path.name
    fig = image.thumbnail(path, outpath, scale=0.15)
    print(f"saved thumbnail of {path} to {outpath}")
```
