# Ausgabeverzeichnis erstellen

In diesem Schritt erstellen Sie ein Verzeichnis namens `thumbs`, in dem die Vorschaubilder gespeichert werden. Wenn das Verzeichnis bereits existiert, wird es nicht erneut erstellt.

```python
outdir = Path("thumbs")
outdir.mkdir(parents=True, exist_ok=True)
```
