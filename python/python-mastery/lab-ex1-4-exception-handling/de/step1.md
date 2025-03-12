# Definition einer Funktion

In diesem Schritt lernen wir, wie man eine Funktion erstellt. Eine Funktion in Python ist ein Block organisierter, wiederverwendbarer Code, der für die Ausführung einer einzelnen, zusammenhängenden Aktion verwendet wird. Hier wird unsere Funktion Portfolio-Daten aus einer Datei lesen und die Gesamtkosten berechnen. Dies ist nützlich, denn sobald wir diese Funktion haben, können wir sie mehrmals mit verschiedenen Portfolio-Dateien verwenden, sodass wir nicht ständig denselben Code schreiben müssen.

## Das Problem verstehen

Im vorherigen Lab haben Sie möglicherweise Code geschrieben, um Portfolio-Daten zu lesen und die Gesamtkosten zu berechnen. Aber dieser Code war wahrscheinlich so geschrieben, dass er nicht einfach wiederverwendet werden kann. Jetzt werden wir diesen Code in eine wiederverwendbare Funktion umwandeln.

Die Portfolio-Daten-Dateien haben ein bestimmtes Format. Sie enthalten Informationen in der Form "Symbol Anzahl Preis". Jede Zeile in der Datei repräsentiert eine Aktienposition. Beispielsweise könnten Sie in einer Datei namens `portfolio.dat` Zeilen wie diese sehen:

```
AA 100 32.20
IBM 50 91.10
...
```

Hier ist der erste Teil (wie "AA" oder "IBM") das Aktiensymbol, das ein eindeutiger Bezeichner für die Aktie ist. Der zweite Teil ist die Anzahl der Aktien, die Sie von dieser Aktie besitzen, und der dritte Teil ist der Preis pro Aktie.

## Die Funktion erstellen

Erstellen wir eine Python-Datei namens `pcost.py` im Verzeichnis `/home/labex/project`. Diese Datei wird unsere Funktion enthalten. Hier ist der Code, den wir in die `pcost.py`-Datei einfügen werden:

```python
def portfolio_cost(filename):
    """
    Berechnet die Gesamtkosten (Anzahl * Preis) einer Portfolio-Datei

    Args:
        filename: Der Name der Portfolio-Datei

    Returns:
        Die Gesamtkosten des Portfolios als Float
    """
    total_cost = 0.0

    # Öffne die Datei und lies jede Zeile
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            # Extrahiere die Daten (Symbol, Anzahl, Preis)
            shares = int(fields[1])
            price = float(fields[2])
            # Füge die Kosten zu unserer laufenden Summe hinzu
            total_cost += shares * price

    return total_cost

# Rufe die Funktion mit der portfolio.dat-Datei auf
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio.dat')
    print(cost)
```

In diesem Code definieren wir zunächst eine Funktion namens `portfolio_cost`, die einen `filename` als Argument nimmt. Innerhalb der Funktion initialisieren wir eine Variable `total_cost` mit 0.0. Dann öffnen wir die Datei mit der `open`-Funktion im Lese-Modus (`'r'`). Wir verwenden eine `for`-Schleife, um jede Zeile in der Datei zu durchlaufen. Für jede Zeile teilen wir sie in Felder auf, indem wir die `split()`-Methode verwenden. Dann extrahieren wir die Anzahl der Aktien und wandeln sie in eine Ganzzahl um, sowie den Preis und wandeln ihn in eine Fließkommazahl um. Wir berechnen die Kosten für diese Aktienposition, indem wir die Anzahl der Aktien mit dem Preis multiplizieren, und fügen sie der `total_cost` hinzu. Schließlich geben wir die `total_cost` zurück.

Der Teil `if __name__ == '__main__':` wird verwendet, um die Funktion aufzurufen, wenn das Skript direkt ausgeführt wird. Wir übergeben den Pfad zur `portfolio.dat`-Datei an die Funktion und geben das Ergebnis aus.

## Die Funktion testen

Jetzt lassen wir das Programm laufen, um zu sehen, ob es funktioniert. Wir müssen in das Verzeichnis navigieren, in dem sich die `pcost.py`-Datei befindet, und dann das Python-Skript ausführen. Hier sind die Befehle dazu:

```bash
cd /home/labex/project
python3 pcost.py
```

Nachdem Sie diese Befehle ausgeführt haben, sollten Sie die Ausgabe sehen:

```
44671.15
```

Diese Ausgabe repräsentiert die Gesamtkosten aller Aktien im Portfolio.

## Den Code verstehen

Lassen Sie uns schrittweise analysieren, was unsere Funktion tut:

1. Sie nimmt einen `filename` als Eingabeparameter. Dies ermöglicht es uns, die Funktion mit verschiedenen Portfolio-Dateien zu verwenden.
2. Sie öffnet die Datei und liest sie Zeile für Zeile. Dies geschieht mit der `open`-Funktion und einer `for`-Schleife.
3. Für jede Zeile teilt sie die Zeile in Felder auf, indem sie die `split()`-Methode verwendet. Diese Methode teilt die Zeile in eine Liste von Strings auf, basierend auf Leerzeichen.
4. Sie wandelt die Anzahl der Aktien in eine Ganzzahl und den Preis in eine Fließkommazahl um. Dies ist notwendig, da die aus der Datei gelesenen Daten im String-Format vorliegen und wir arithmetische Operationen darauf ausführen müssen.
5. Sie berechnet die Kosten (Anzahl \* Preis) für jede Aktienposition und fügt sie der laufenden Summe hinzu. Dies ergibt uns die Gesamtkosten des Portfolios.
6. Sie gibt die endgültigen Gesamtkosten zurück. Dies ermöglicht es uns, das Ergebnis bei Bedarf in anderen Teilen unseres Programms zu verwenden.

Diese Funktion ist jetzt wiederverwendbar. Wir können sie mit verschiedenen Portfolio-Dateien aufrufen, um deren Kosten zu berechnen, was unseren Code effizienter und leichter zu warten macht.
