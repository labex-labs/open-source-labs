# Übung 6.6: Verwenden eines Generators zum Erzeugen von Daten

Wenn Sie sich den Code in Übung 6.5 ansehen, produziert der erste Teil des Codes Zeilen von Daten, während die Anweisungen am Ende der `while`-Schleife die Daten verarbeiten. Ein wichtiges Merkmal von Generatorfunktionen ist, dass Sie den gesamten Datenproduktionscode in eine wiederverwendbare Funktion verschieben können.

Ändern Sie den Code in Übung 6.5 so, dass das Lesen der Datei von einer Generatorfunktion `follow(filename)` durchgeführt wird. Stellen Sie sicher, dass der folgende Code funktioniert:

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... Sollte hier Zeilen von Ausgabe sehen...
```

Ändern Sie den Aktien-Ticker-Code so, dass er wie folgt aussieht:

```python
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```
