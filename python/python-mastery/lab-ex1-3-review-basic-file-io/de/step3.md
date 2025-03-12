# Verarbeitung der Daten

Nachdem wir gelernt haben, wie man eine Datei liest, ist der nächste Schritt, jede Zeile der Datei zu verarbeiten, um die Kosten jedes Aktienkaufs zu berechnen. Dies ist ein wichtiger Teil der Arbeit mit Daten in Python, da es uns ermöglicht, sinnvolle Informationen aus der Datei zu extrahieren.

Jede Zeile in der Datei folgt einem bestimmten Format: `[Stock Symbol] [Number of Shares] [Price per Share]`. Um die Kosten jedes Aktienkaufs zu berechnen, müssen wir die Anzahl der Aktien und den Preis pro Aktie aus jeder Zeile extrahieren. Dann multiplizieren wir diese beiden Werte miteinander, um die Kosten dieses bestimmten Aktienkaufs zu erhalten. Schließlich addieren wir diese Kosten zu unserem laufenden Gesamtbetrag, um die Gesamtkosten des Portfolios zu ermitteln.

Lassen Sie uns die `portfolio_cost()`-Funktion in der `pcost.py`-Datei ändern, um dies zu erreichen. Hier ist der geänderte Code:

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            # Strip any leading/trailing whitespace
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Split the line into fields
            fields = line.split()

            # Extract the relevant data
            # fields[0] is the stock symbol (which we don't need for the calculation)
            shares = int(fields[1])  # Number of shares (second field)
            price = float(fields[2])  # Price per share (third field)

            # Calculate the cost of this stock purchase
            cost = shares * price

            # Add to the total cost
            total_cost += cost

            # Print some debug information
            print(f'{fields[0]}: {shares} shares at ${price:.2f} = ${cost:.2f}')

    # Return the total cost
    return total_cost
```

Lassen Sie uns schrittweise analysieren, was diese geänderte Funktion tut:

1. **Entfernt Leerzeichen**: Wir verwenden die `strip()`-Methode, um alle führenden oder nachfolgenden Leerzeichen von jeder Zeile zu entfernen. Dies stellt sicher, dass wir keine zusätzlichen Leerzeichen versehentlich einbeziehen, wenn wir die Zeile in Felder aufteilen.
2. **Überspringt leere Zeilen**: Wenn eine Zeile leer ist (d. h., sie enthält nur Leerzeichen), verwenden wir die `continue`-Anweisung, um sie zu überspringen. Dies hilft uns, Fehler zu vermeiden, wenn wir versuchen, eine leere Zeile zu teilen.
3. **Teilt die Zeile in Felder auf**: Wir verwenden die `split()`-Methode, um jede Zeile in eine Liste von Feldern auf der Grundlage von Leerzeichen aufzuteilen. Dies ermöglicht es uns, jeden Teil der Zeile separat zuzugreifen.
4. **Extrahiert relevante Daten**: Wir extrahieren die Anzahl der Aktien und den Preis pro Aktie aus der Liste der Felder. Die Anzahl der Aktien ist das zweite Feld, und der Preis pro Aktie ist das dritte Feld. Wir konvertieren diese Werte in die entsprechenden Datentypen (`int` für die Anzahl der Aktien und `float` für den Preis), damit wir arithmetische Operationen darauf ausführen können.
5. **Berechnet die Kosten**: Wir multiplizieren die Anzahl der Aktien mit dem Preis pro Aktie, um die Kosten dieses Aktienkaufs zu berechnen.
6. **Addiert zum Gesamtbetrag**: Wir addieren die Kosten dieses Aktienkaufs zum laufenden Gesamtbetrag.
7. **Gibt Debug-Informationen aus**: Wir geben einige Informationen über jeden Aktienkauf aus, um zu sehen, was passiert. Dies umfasst das Aktiensymbol, die Anzahl der Aktien, den Preis pro Aktie und die Gesamtkosten des Kaufs.

Nun lassen wir den Code laufen, um zu sehen, ob er funktioniert. Öffnen Sie Ihr Terminal und führen Sie den folgenden Befehl aus:

```bash
python3 ~/project/pcost.py
```

Nachdem Sie den Befehl ausgeführt haben, sollten Sie detaillierte Informationen über jeden Aktienkauf sehen, gefolgt von den Gesamtkosten des Portfolios. Diese Ausgabe wird Ihnen helfen, zu überprüfen, ob die Funktion korrekt funktioniert und ob Sie die Gesamtkosten genau berechnet haben.
