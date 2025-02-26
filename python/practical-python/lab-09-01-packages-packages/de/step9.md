# Ein weiterer Lösung für Skripte

Wie erwähnt, müssen Sie jetzt `-m package.module` verwenden, um Skripte innerhalb Ihres Pakets auszuführen.

```bash
$ python3 -m porty.pcost portfolio.csv
```

Es gibt eine weitere Möglichkeit: Schreiben Sie ein neues Hauptskript.

```python
#!/usr/bin/env python3
# pcost.py
import porty.pcost
import sys
porty.pcost.main(sys.argv)
```

Dieses Skript befindet sich _außerhalb_ des Pakets. Beispielsweise betrachten Sie die Verzeichnisstruktur:

    pcost.py       # Hauptskript
    porty/         # Paketverzeichnis
        __init__.py
        pcost.py
     ...
