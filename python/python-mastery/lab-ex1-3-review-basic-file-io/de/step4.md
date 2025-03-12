# Abschluss des Programms

Jetzt werden wir unseren Code aufräumen und die endgültige Version des `pcost.py`-Programms erstellen. Das Aufräumen des Codes bedeutet, alle unnötigen Teile zu entfernen und sicherzustellen, dass die Ausgabe gut aussieht. Dies ist ein wichtiger Schritt in der Programmierung, da es unseren Code professioneller und leichter verständlich macht.

Wir beginnen damit, die Debug-Ausgabebefehle zu entfernen. Diese Befehle werden während der Entwicklung verwendet, um die Werte von Variablen und den Programmablauf zu überprüfen, aber sie sind in der endgültigen Version nicht erforderlich. Dann stellen wir sicher, dass die endgültige Ausgabe schön formatiert ist.

Hier ist die endgültige Version des `pcost.py`-Codes:

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    try:
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

                # Calculate the cost of this stock purchase and add to the total
                total_cost += shares * price

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return 0.0
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0.0

    # Return the total cost
    return total_cost

# Main block to run when the script is executed directly
if __name__ == '__main__':
    # Call the function with the portfolio file
    total_cost = portfolio_cost('portfolio.dat')
    print(f'Total cost: ${total_cost:.2f}')
```

Diese endgültige Version des Codes hat mehrere Verbesserungen:

1. Fehlerbehandlung: Wir haben Code hinzugefügt, um zwei Arten von Fehlern abzufangen. Der `FileNotFoundError` wird ausgelöst, wenn die angegebene Datei nicht existiert. Wenn dies geschieht, gibt das Programm eine Fehlermeldung aus und gibt 0,0 zurück. Der `Exception`-Block fängt alle anderen Fehler ab, die beim Verarbeiten der Datei auftreten können. Dies macht unser Programm robuster und weniger anfällig für unerwartete Abstürze.
2. Korrekte Formatierung: Die Gesamtkosten werden mit dem `:.2f`-Format-Spezifizierer in der f-String auf zwei Dezimalstellen formatiert. Dies macht die Ausgabe professioneller und leichter lesbar.
3. `__name__ == '__main__'`-Prüfung: Dies ist ein gängiges Python-Idiom. Es stellt sicher, dass der Code innerhalb des `if`-Blocks nur ausgeführt wird, wenn das Skript direkt ausgeführt wird. Wenn das Skript als Modul in ein anderes Skript importiert wird, wird dieser Code nicht ausgeführt. Dies gibt uns mehr Kontrolle darüber, wie unser Skript verhält.

Jetzt lassen wir den endgültigen Code laufen. Öffnen Sie Ihr Terminal und geben Sie den folgenden Befehl ein:

```bash
python3 ~/project/pcost.py
```

Wenn Sie diesen Befehl ausführen, liest das Programm die `portfolio.dat`-Datei, berechnet die Gesamtkosten des Portfolios und gibt das Ergebnis aus. Sie sollten die Gesamtkosten des Portfolios sehen, die $44671,15 betragen sollten.

Herzlichen Glückwunsch! Sie haben erfolgreich ein Python-Programm erstellt, das Daten aus einer Datei liest, verarbeitet und ein Ergebnis berechnet. Dies ist ein großartiges Erreichen und zeigt, dass Sie auf dem Weg sind, ein versierter Python-Programmierer zu werden.
