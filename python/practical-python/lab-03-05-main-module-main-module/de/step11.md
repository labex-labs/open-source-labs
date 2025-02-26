# Die `#!`-Zeile

Auf Unix kann die `#!`-Zeile ein Skript als Python starten. Fügen Sie Folgendes zur ersten Zeile Ihrer Skriptdatei hinzu.

```python
#!/usr/bin/env python3
#./prog.py
...
```

Es erfordert die Ausführbarkeitsberechtigung.

```bash
$ chmod +x prog.py
# Dann können Sie ausführen
$./prog.py
... Ausgabe...
```

_Hinweis: Der Python-Launcher unter Windows sucht ebenfalls nach der `#!`-Zeile, um die Sprachversion anzugeben._
