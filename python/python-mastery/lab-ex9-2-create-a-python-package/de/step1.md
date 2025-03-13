# Python-Pakete verstehen

Bevor wir mit der Erstellung eines Python-Pakets beginnen, lernen wir zunächst, was ein Python-Paket ist. Ein Python-Paket ist im Wesentlichen ein Verzeichnis. Innerhalb dieses Verzeichnisses befinden sich mehrere Python-Moduldateien, die einfach `.py`-Dateien mit Python-Code sind. Zusätzlich gibt es eine spezielle Datei namens `__init__.py`. Diese Datei kann leer sein, aber ihre Existenz zeigt an, dass das Verzeichnis ein Python-Paket ist. Das Ziel dieser Struktur ist es, Ihnen zu helfen, verwandten Code in einer einzigen Verzeichnis-Hierarchie zu organisieren.

Pakete bieten mehrere Vorteile. Erstens ermöglichen sie es Ihnen, Ihren Code logisch zu strukturieren. Anstatt alle Ihre Python-Dateien überall verteilt zu haben, können Sie verwandte Funktionen in einem Paket zusammenfassen. Zweitens helfen sie dabei, Namenskonflikte zwischen Modulen zu vermeiden. Da Pakete einen Namensraum (namespace) erstellen, können Sie Module mit demselben Namen in verschiedenen Paketen haben, ohne dass es Probleme gibt. Drittens machen sie das Importieren und Verwenden Ihres Codes bequemer. Sie können ganz einfach ein gesamtes Paket oder bestimmte Module daraus importieren.

Nun schauen wir uns die Dateien an, die sich derzeit in unserem Projektverzeichnis befinden. Um die Dateien aufzulisten, verwenden wir den folgenden Befehl im Terminal:

```bash
ls -l
```

Wenn Sie diesen Befehl ausführen, sollten Sie die folgenden Dateien sehen:

```
portfolio.csv
reader.py
stock.py
structure.py
tableformat.py
validate.py
```

Diese Python-Dateien sind alle verwandt und arbeiten zusammen, aber derzeit sind es nur separate Module. In diesem Lab ist unser Ziel, sie zu einem zusammenhängenden Paket namens `structly` zu organisieren.

Lassen Sie uns kurz verstehen, was jede Datei macht:

- `structure.py`: Diese Datei definiert eine Basisklasse `Structure` und verschiedene Deskriptoren (descriptors). Diese Deskriptoren werden zur Typüberprüfung (type validation) verwendet, was bedeutet, dass sie helfen, sicherzustellen, dass die im Programm verwendeten Daten den richtigen Typ haben.
- `validate.py`: Sie enthält Validierungsfunktionen, die vom `structure`-Modul verwendet werden. Dies hilft bei der Überprüfung der Daten gemäß bestimmten Regeln.
- `reader.py`: Diese Datei bietet Funktionen, die zum Lesen von CSV-Daten verwendet werden. CSV (Comma-Separated Values) ist ein gängiges Dateiformat zum Speichern tabellarischer Daten.
- `tableformat.py`: Sie enthält Klassen und Funktionen, die zum Formatieren von Daten in Tabellen verwendet werden. Dies ist nützlich, wenn Sie Daten auf eine organisiertere Weise anzeigen möchten.
- `stock.py`: Diese Datei verwendet die anderen Module, um eine `Stock`-Klasse zu definieren und Aktiendaten zu verarbeiten. Sie kombiniert die Funktionen der anderen Module, um bestimmte Aufgaben im Zusammenhang mit Aktiendaten auszuführen.

Im nächsten Schritt erstellen wir unsere Paketstruktur.
