# Die Anwendung erstellen

Zunächst müssen wir eine Wheel-Datei für unsere Anwendung erstellen. Dazu verwenden wir das `build`-Tool. Installieren Sie das `build`-Tool mit pip, wenn Sie es noch nicht getan haben:

```bash
# Installieren Sie das build-Tool
pip install build
```

Verwenden Sie nun das `build`-Tool, um die Wheel-Datei zu erstellen:

```bash
# Erstellen Sie die Wheel-Datei
python -m build --wheel
```

Die Wheel-Datei sollte sich im `dist`-Verzeichnis befinden und einen Namen wie `flaskr-1.0.0-py3-none-any.whl` haben.
