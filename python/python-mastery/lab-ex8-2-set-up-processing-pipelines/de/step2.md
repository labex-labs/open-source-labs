# Erstellen der Ticker-Klasse

Bei der Datenverarbeitung kann die Arbeit mit Rohdaten recht herausfordernd sein. Um unsere Arbeit mit Aktiendaten organisierter und effizienter zu gestalten, definieren wir eine geeignete Klasse, um Aktienkurse darzustellen. Diese Klasse dient als Blaupause für unsere Aktiendaten und macht unsere Datenverarbeitungspipeline robuster und einfacher zu verwalten.

## Erstellen der ticker.py-Datei

1. Zunächst müssen wir eine neue Datei in der WebIDE erstellen. Dies können Sie tun, indem Sie auf das Symbol "New File" klicken oder mit der rechten Maustaste im Dateiexplorer klicken und "New File" auswählen. Benennen Sie diese Datei `ticker.py`. In dieser Datei wird der Code für unsere `Ticker`-Klasse gespeichert.

2. Fügen Sie nun den folgenden Code in Ihre neu erstellte `ticker.py`-Datei ein. Dieser Code definiert unsere `Ticker`-Klasse und richtet eine einfache Verarbeitungspipeline ein, um sie zu testen.

```python
# ticker.py

from structure import Structure, String, Float, Integer

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

if __name__ == '__main__':
    from follow import follow
    import csv
    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    for record in records:
        print(record)
```

3. Nachdem Sie den Code hinzugefügt haben, speichern Sie die Datei. Dies können Sie tun, indem Sie `Strg+S` drücken oder im Menü "File" → "Save" auswählen. Das Speichern der Datei stellt sicher, dass Ihre Änderungen gespeichert werden und später ausgeführt werden können.

## Verständnis des Codes

Schauen wir uns genauer an, was dieser Code Schritt für Schritt macht:

1. Am Anfang des Codes importieren wir `Structure` und Feldtypen aus dem `structure.py`-Modul. Dieses Modul wurde bereits für Sie eingerichtet. Diese Importe sind wichtig, da sie die Bausteine für unsere `Ticker`-Klasse bereitstellen. Die `Structure`-Klasse wird die Basisklasse für unsere `Ticker`-Klasse sein, und die Feldtypen wie `String`, `Float` und `Integer` werden die Datentypen unserer Aktiendatenfelder definieren.

2. Als Nächstes definieren wir eine `Ticker`-Klasse, die von `Structure` erbt. Diese Klasse hat mehrere Felder, die verschiedene Aspekte der Aktiendaten darstellen:
   - `name`: Dieses Feld speichert das Aktiensymbol, wie z.B. "IBM" oder "AAPL". Es hilft uns zu identifizieren, für welche Firma wir die Aktien verarbeiten.
   - `price`: Es enthält den aktuellen Preis der Aktie. Dies ist eine entscheidende Information für Anleger.
   - `date` und `time`: Diese Felder geben an, wann der Aktienkurs erstellt wurde. Das Wissen um Zeit und Datum ist wichtig für die Analyse von Aktienkurs-Trends über die Zeit.
   - `change`: Dies repräsentiert die Preisänderung der Aktie. Es zeigt, ob der Aktienpreis im Vergleich zu einem früheren Zeitpunkt gestiegen oder gefallen ist.
   - `open`, `high`, `low`: Diese Felder repräsentieren den Eröffnungspreis, den höchsten Preis und den niedrigsten Preis der Aktie während eines bestimmten Zeitraums. Sie geben uns eine Vorstellung von der Preisspanne der Aktie.
   - `volume`: Dieses Feld speichert die Anzahl der gehandelten Aktien. Ein hoher Handelsvolumen kann auf ein starkes Marktinteresse an einer bestimmten Aktie hinweisen.

3. Im `if __name__ == '__main__':`-Block richten wir eine Verarbeitungspipeline ein. Dieser Codeblock wird ausgeführt, wenn wir die `ticker.py`-Datei direkt ausführen.
   - `follow('stocklog.csv')` ist eine Funktion, die Zeilen aus der `stocklog.csv`-Datei erzeugt. Sie ermöglicht es uns, die Datei zeilenweise zu lesen.
   - `csv.reader(lines)` nimmt diese Zeilen und parst sie in Zeildaten. CSV (Comma - Separated Values) ist ein gängiges Dateiformat zum Speichern tabellarischer Daten, und diese Funktion hilft uns, die Daten aus jeder Zeile zu extrahieren.
   - `(Ticker.from_row(row) for row in rows)` ist ein Generatorausdruck. Er nimmt jede Zeile der Daten und wandelt sie in ein `Ticker`-Objekt um. Auf diese Weise transformieren we die Roh-CSV-Daten in strukturierte Objekte, mit denen es einfacher zu arbeiten ist.
   - Die `for`-Schleife iteriert über diese `Ticker`-Objekte und gibt jedes Objekt aus. Dies ermöglicht es uns, die strukturierten Daten in Aktion zu sehen.

## Ausführen des Codes

Lassen Sie uns den Code ausführen, um zu sehen, wie er funktioniert:

1. Zunächst müssen wir sicherstellen, dass wir im Terminal im Projektverzeichnis sind. Wenn Sie noch nicht dort sind, verwenden Sie den folgenden Befehl, um dorthin zu navigieren:

   ```bash
   cd /home/labex/project
   ```

2. Sobald Sie sich im richtigen Verzeichnis befinden, führen Sie das `ticker.py`-Skript mit dem folgenden Befehl aus:

   ```bash
   python3 ticker.py
   ```

3. Nach dem Ausführen des Skripts sollten Sie eine Ausgabe ähnlich der folgenden sehen (Ihre Daten werden variieren):
   ```
   Ticker(IBM, 103.53, 6/11/2007, 09:53.59, 0.46, 102.87, 103.53, 102.77, 541633)
   Ticker(MSFT, 30.21, 6/11/2007, 09:54.01, 0.16, 30.05, 30.21, 29.95, 7562516)
   Ticker(AA, 40.01, 6/11/2007, 09:54.01, 0.35, 39.67, 40.15, 39.31, 576619)
   Ticker(T, 40.1, 6/11/2007, 09:54.08, -0.16, 40.2, 40.19, 39.87, 1312959)
   ```

Sie können die Ausführung des Skripts stoppen, indem Sie `Strg+C` drücken, wenn Sie genug Ausgabe gesehen haben.

Beachten Sie, wie die Roh-CSV-Daten in strukturierte `Ticker`-Objekte transformiert wurden. Diese Transformation macht es viel einfacher, mit den Daten in unserer Verarbeitungspipeline zu arbeiten, da wir jetzt die Aktiendaten über die in der `Ticker`-Klasse definierten Felder zugreifen und manipulieren können.
