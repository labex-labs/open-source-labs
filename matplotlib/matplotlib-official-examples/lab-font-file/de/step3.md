# Setzen des Schriftartpfads

Wir setzen den Schriftartpfad, indem wir die `mpl.get_data_path()`-Methode verwenden, um den Pfad des Datenverzeichnisses zu erhalten, und fügen dann den Pfad zur Schriftartdatei `cmr10.ttf` hinzu, indem wir die `Path()`-Methode aus dem `pathlib`-Modul verwenden.

```python
from pathlib import Path

fpath = Path(mpl.get_data_path(), "fonts/ttf/cmr10.ttf")
```
