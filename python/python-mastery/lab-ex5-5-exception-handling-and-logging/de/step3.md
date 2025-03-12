# Implementierung der Protokollierung (Logging)

In diesem Schritt werden wir Ihren Code verbessern. Anstatt einfache `print`-Nachrichten zu verwenden, nutzen wir das `logging`-Modul von Python für eine ordnungsgemäße Protokollierung. Die Protokollierung ist eine ausgezeichnete Methode, um zu verfolgen, was Ihr Programm tut, insbesondere wenn es um die Fehlerbehandlung und das Verständnis des Programmablaufs geht.

## Grundlagen des Logging-Moduls

Das `logging`-Modul in Python bietet uns eine flexible Möglichkeit, Protokollnachrichten aus unseren Anwendungen zu senden. Es ist viel leistungsstärker als die einfache Verwendung von `print`-Anweisungen. Hier ist, was es kann:

1. Verschiedene Log-Level (DEBUG, INFO, WARNING, ERROR, CRITICAL): Diese Level helfen uns, die Wichtigkeit der Nachrichten zu kategorisieren. Beispielsweise ist DEBUG für detaillierte Informationen gedacht, die während der Entwicklung nützlich sind, während CRITICAL für ernsthafte Fehler steht, die das Programm möglicherweise stoppen können.
2. Konfigurierbares Ausgabeformat: Wir können entscheiden, wie die Protokollnachrichten aussehen sollen, z. B. indem wir Zeitstempel oder andere nützliche Informationen hinzufügen.
3. Nachrichten können an verschiedene Ausgaben gerichtet werden (Konsole, Dateien usw.): Wir können auswählen, ob die Protokollnachrichten auf der Konsole angezeigt, in einer Datei gespeichert oder sogar an einen Remote-Server gesendet werden sollen.
4. Log-Filterung basierend auf der Schweregrad: Wir können steuern, welche Nachrichten wir sehen, basierend auf ihrem Log-Level.

## Hinzufügen der Protokollierung zu reader.py

Jetzt ändern wir Ihren Code, um das `logging`-Modul zu verwenden. Öffnen Sie die Datei `reader.py`.

Zunächst müssen wir das `logging`-Modul importieren und einen Logger für dieses Modul einrichten. Fügen Sie den folgenden Code oben in der Datei hinzu:

```python
import logging

# Set up a logger for this module
logger = logging.getLogger(__name__)
```

Die Anweisung `import logging` importiert das `logging`-Modul, damit wir seine Funktionen verwenden können. `logging.getLogger(__name__)` erstellt einen Logger für dieses spezifische Modul. Die Verwendung von `__name__` stellt sicher, dass der Logger einen eindeutigen Namen hat, der mit dem Modul verbunden ist.

Als Nächstes ändern wir die Funktion `convert_csv()`, um die Protokollierung anstelle von `print`-Anweisungen zu verwenden. Hier ist der aktualisierte Code:

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Log a warning message for bad rows
            logger.warning(f"Row {row_idx}: Bad row: {row}")
            # Log the reason at debug level
            logger.debug(f"Row {row_idx}: Reason: {str(e)}")
            continue

    return result
```

Die Hauptänderungen sind:

- Wir haben `print()` durch `logger.warning()` für die Fehlermeldung ersetzt. Auf diese Weise wird die Nachricht mit dem entsprechenden Warn-Level protokolliert, und wir können später ihre Sichtbarkeit steuern.
- Wir haben eine neue `logger.debug()`-Nachricht mit Details zur Ausnahme hinzugefügt. Dies gibt uns mehr Informationen darüber, was schief gelaufen ist, aber es wird nur angezeigt, wenn das Log-Level auf DEBUG oder niedriger eingestellt ist.
- `str(e)` wandelt die Ausnahme in einen String um, so dass wir den Fehlergrund in der Protokollnachricht anzeigen können.

Nach diesen Änderungen speichern Sie die Datei.

## Testen der Protokollierung

Testen wir Ihren Code mit aktivierter Protokollierung. Öffnen Sie den Python-Interpreter, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:

```bash
python3
```

Sobald Sie sich im Python-Interpreter befinden, führen Sie den folgenden Code aus:

```python
import logging
import reader

# Configure logging level to see all messages
logging.basicConfig(level=logging.DEBUG)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

Hier importieren wir zunächst das `logging`-Modul und unser `reader`-Modul. Dann setzen wir das Log-Level auf DEBUG mit `logging.basicConfig(level=logging.DEBUG)`. Dies bedeutet, dass wir alle Protokollnachrichten sehen werden, einschließlich DEBUG, INFO, WARNING, ERROR und CRITICAL. Anschließend rufen wir die Funktion `read_csv_as_dicts` aus dem `reader`-Modul auf und geben die Anzahl der verarbeiteten gültigen Zeilen aus.

Sie sollten eine Ausgabe wie diese sehen:

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
DEBUG:reader:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
DEBUG:reader:Row 7: Reason: could not convert string to float: 'N/A'
...
Number of valid rows processed: 20
```

Beachten Sie, dass das `logging`-Modul jedem Nachrichten einen Präfix hinzufügt, der das Log-Level (WARNING/DEBUG) und den Modulnamen anzeigt.

Jetzt schauen wir uns an, was passiert, wenn wir das Log-Level so ändern, dass nur Warnungen angezeigt werden. Führen Sie den folgenden Code im Python-Interpreter aus:

```python
# Reset the logging configuration
import logging
logging.basicConfig(level=logging.WARNING)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
```

Diesmal setzen wir das Log-Level auf WARNING mit `logging.basicConfig(level=logging.WARNING)`. Jetzt werden Sie nur die WARNING-Nachrichten sehen, und die DEBUG-Nachrichten werden ausgeblendet:

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
...
```

Dies zeigt den Vorteil der Verwendung verschiedener Log-Level. Wir können steuern, wie viel Detail in den Protokollen angezeigt wird, ohne unseren Code zu ändern.

Um den Python-Interpreter zu beenden, führen Sie den folgenden Befehl aus:

```python
exit()
```

Herzlichen Glückwunsch! Sie haben jetzt eine ordnungsgemäße Ausnahmebehandlung und Protokollierung in Ihrem Python-Programm implementiert. Dies macht Ihren Code zuverlässiger und gibt Ihnen bessere Informationen, wenn Fehler auftreten.
