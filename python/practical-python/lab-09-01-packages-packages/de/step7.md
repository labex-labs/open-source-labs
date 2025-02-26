# Problem: Main Scripts

Das Ausführen eines Paket-Untermoduls als Hauptskript bricht.

```bash
$ python porty/pcost.py # Bricht
...
```

_Grund: Sie führen Python auf einer einzelnen Datei aus und Python erkennt die restliche Paketstruktur nicht richtig (`sys.path` ist falsch)._

Alle Imports brechen. Um das zu beheben, müssen Sie Ihr Programm auf eine andere Weise ausführen, indem Sie die Option `-m` verwenden.

```bash
$ python -m porty.pcost # Funktioniert
...
```
