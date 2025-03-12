# Aufbau einer komplexeren Datenpipeline

Jetzt werden wir unsere Datenpipeline auf die nächste Stufe heben, indem wir Filterung hinzufügen und die Darstellung der Daten verbessern. Dies wird es einfacher machen, die Informationen, mit denen wir arbeiten, zu analysieren und zu verstehen. Wir werden Änderungen an unserem `ticker.py`-Skript vornehmen. Die Filterung der Daten hilft uns, uns auf die spezifischen Informationen zu konzentrieren, an denen wir interessiert sind, und die Darstellung in einer schön formatierten Tabelle macht die Daten lesbarer.

## Aktualisieren der ticker.py-Datei

1. Öffnen Sie zunächst Ihre `ticker.py`-Datei in der WebIDE. Die WebIDE ist ein Tool, das es Ihnen ermöglicht, direkt in Ihrem Browser Code zu schreiben und zu bearbeiten. Sie bietet eine bequeme Umgebung für die Änderung Ihrer Python-Skripte.

2. Als Nächstes müssen wir den `if __name__ == '__main__':`-Block in der `ticker.py`-Datei durch den folgenden Code ersetzen. Dieser Codeblock ist der Einstiegspunkt unseres Skripts, und durch seine Ersetzung ändern wir, wie das Skript die Daten verarbeitet und anzeigt.

```python
if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name', 'price', 'change'], formatter)
```

3. Nachdem Sie diese Änderungen vorgenommen haben, speichern Sie die Datei. Dies können Sie tun, indem Sie `Strg+S` auf Ihrer Tastatur drücken oder im Menü "File" → "Save" auswählen. Das Speichern der Datei stellt sicher, dass Ihre Änderungen gespeichert werden und später ausgeführt werden können.

## Verständnis der erweiterten Pipeline

Schauen wir uns genauer an, was diese erweiterte Pipeline tut. Das Verständnis jeder Stufe hilft Ihnen zu verstehen, wie die verschiedenen Teile des Codes zusammenarbeiten, um die Daten zu verarbeiten und anzuzeigen.

1. Wir beginnen damit, `create_formatter` und `print_table` aus dem `tableformat`-Modul zu importieren. Dieses Modul ist bereits für Sie eingerichtet und bietet Funktionen, die uns helfen, die Daten in einer schönen Tabelle zu formatieren und auszugeben.

2. Dann erstellen wir einen Text-Formatter mit `create_formatter('text')`. Dieser Formatter wird verwendet, um die Daten auf eine leicht lesbare Weise zu formatieren.

3. Jetzt zerlegen wir die Pipeline Schritt für Schritt:
   - `follow('stocklog.csv')` ist eine Funktion, die Zeilen aus der `stocklog.csv`-Datei erzeugt. Sie überwacht kontinuierlich die Datei auf neue Daten und liefert die Zeilen nacheinander.
   - `csv.reader(lines)` nimmt die von `follow` erzeugten Zeilen und parst sie in Zeildaten. Dies ist notwendig, da die Daten in der CSV-Datei in Textform vorliegen und wir sie in ein strukturiertes Format umwandeln müssen, mit dem wir arbeiten können.
   - `(Ticker.from_row(row) for row in rows)` ist ein Generatorausdruck, der jede Zeile der Daten in ein `Ticker`-Objekt umwandelt. Ein `Ticker`-Objekt repräsentiert eine Aktie und enthält Informationen wie den Namen, den Preis und die Änderung der Aktie.
   - `(rec for rec in records if rec.change < 0)` ist ein weiterer Generatorausdruck, der die `Ticker`-Objekte filtert. Er behält nur die Objekte, bei denen die Preisänderung der Aktie negativ ist. Dies ermöglicht es uns, uns auf die Aktien zu konzentrieren, deren Preis gefallen ist.
   - `print_table(negative, ['name', 'price', 'change'], formatter)` nimmt die gefilterten `Ticker`-Objekte und formatiert sie in eine Tabelle mit dem von uns zuvor erstellten Formatter. Anschließend gibt es die Tabelle in der Konsole aus.

Diese Pipeline zeigt die Stärke von Generatoren. Anstatt alle Daten aus der Datei auf einmal in den Speicher zu laden, verketten wir mehrere Operationen (Lesen, Parsen, Konvertieren, Filtern) und verarbeiten die Daten Stück für Stück. Dies spart Speicher und macht den Code effizienter.

## Ausführen der erweiterten Pipeline

Lassen Sie uns den aktualisierten Code ausführen, um die Ergebnisse zu sehen.

1. Stellen Sie zunächst sicher, dass Sie sich im Terminal im Projektverzeichnis befinden. Wenn Sie noch nicht dort sind, können Sie dorthin navigieren, indem Sie den folgenden Befehl verwenden:

   ```bash
   cd /home/labex/project
   ```

2. Sobald Sie sich im Projektverzeichnis befinden, führen Sie das `ticker.py`-Skript mit dem folgenden Befehl aus:

   ```bash
   python3 ticker.py
   ```

3. Nach dem Ausführen des Skripts sollten Sie in der Terminal eine schön formatierte Tabelle sehen. Diese Tabelle zeigt nur die Aktien mit negativen Preisänderungen.

   ```
          name      price     change
    ---------- ---------- ----------
             C      53.12      -0.21
           UTX      70.04      -0.19
           AXP      62.86      -0.18
           MMM      85.72      -0.22
           MCD      51.38      -0.03
           WMT      49.85      -0.23
            KO       51.6      -0.07
           AIG      71.39      -0.14
            PG      63.05      -0.02
            HD      37.76      -0.19
   ```

Wenn Sie genug Ausgabe gesehen haben und die Ausführung des Skripts beenden möchten, können Sie `Strg+C` auf Ihrer Tastatur drücken.

## Die Stärke von Generator-Pipelines

Was wir hier erstellt haben, ist eine leistungsstarke Datenverarbeitungspipeline. Lassen Sie uns zusammenfassen, was sie tut:

1. Sie überwacht kontinuierlich die `stocklog.csv`-Datei auf neue Daten. Dies bedeutet, dass die Pipeline automatisch neue Daten verarbeitet, sobald sie zur Datei hinzugefügt werden.
2. Sie parst die CSV-Daten aus der Datei in strukturierte `Ticker`-Objekte. Dies erleichtert die Arbeit mit den Daten und die Ausführung von Operationen darauf.
3. Sie filtert die Daten basierend auf einem bestimmten Kriterium, in diesem Fall negativen Preisänderungen. Dies ermöglicht es uns, uns auf die Aktien zu konzentrieren, die an Wert verlieren.
4. Sie formatiert und präsentiert die gefilterten Daten in einer lesbaren Tabelle. Dies erleichtert die Analyse der Daten und das Ziehen von Schlussfolgerungen.

Einer der Hauptvorteile der Verwendung von Generatoren in dieser Pipeline ist, dass sie minimalen Speicherplatz benötigt. Generatoren erzeugen Werte bedarfsweise, was bedeutet, dass sie nicht alle Daten auf einmal im Speicher speichern. Dies ähnelt Unix-Pipes, bei denen jede Komponente die Daten verarbeitet und an die nächste Komponente weitergibt.

Sie können sich Generatoren als Lego-Bausteine vorstellen. Genau wie Sie Lego-Bausteine stapeln können, um verschiedene Strukturen zu erstellen, können Sie Generatoren kombinieren, um leistungsstarke Datenverarbeitungsabläufe zu erstellen. Dieser modulare Ansatz ermöglicht es Ihnen, komplexe Systeme aus einfachen, wiederverwendbaren Komponenten aufzubauen.
