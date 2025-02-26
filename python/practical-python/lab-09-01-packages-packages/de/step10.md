# Anwendungsstruktur

Die Codeorganisation und die Dateistruktur sind entscheidend für die Wartbarkeit einer Anwendung.

Es gibt keine "eines-fits-all"-Methode für Python. Ein Struktur, die jedoch für viele Probleme funktioniert, sieht so aus.

```code
porty-app/
  README.txt
  script.py         # SKRIPT
  porty/
    # BIBLIOTHEKSCODE
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Das oberste Level `porty-app` ist ein Container für alles andere - Dokumentation, oberste Level Skripte, Beispiele usw.

Wiederholen Sie, dass die obersten Level Skripte (falls vorhanden) außerhalb des Code-Pakets existieren müssen. Ein Level höher.

```python
#!/usr/bin/env python3
# porty-app/script.py
import sys
import porty

porty.report.main(sys.argv)
```

Zu diesem Zeitpunkt haben Sie ein Verzeichnis mit mehreren Programmen:

    pcost.py          # berechnet die Portfolio-Kosten
    report.py         # Erstellt einen Bericht
    ticker.py         # Erzeugt einen Echtzeit-Aktien-Ticker

Es gibt eine Vielzahl von unterstützenden Modulen mit anderen Funktionen:

    stock.py          # Stock-Klasse
    portfolio.py      # Portfolio-Klasse
    fileparse.py      # CSV-Parsing
    tableformat.py    # Formatierte Tabellen
    follow.py         # Folgt einer Log-Datei
    typedproperty.py  # Typisierte Klassen-Eigenschaften

In dieser Übung werden wir den Code aufräumen und in ein gemeinsames Paket einfügen.
