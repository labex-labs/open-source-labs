# Argumente analysieren

In diesem Schritt werden Sie die an Ihr Programm übergebenen Argumente analysieren. Sie müssen ein `ArgumentParser`-Objekt erstellen und ein Argument namens `imagedir` hinzufügen. Dieses Argument gibt den Pfad zum Verzeichnis an, das die Bilder enthält. Sie können den `type`-Parameter verwenden, um den Datentyp des Arguments anzugeben. In diesem Fall sollte das Argument vom Typ `Path` sein.

```python
parser = ArgumentParser(description="Build thumbnails of all images in a directory.")
parser.add_argument("imagedir", type=Path)
args = parser.parse_args()
```
