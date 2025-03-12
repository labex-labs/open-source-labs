# Öffnen und Lesen der Datei

In diesem Schritt werden wir lernen, wie man in Python eine Datei öffnet und liest. Dateieingabe/Ausgabe (I/O) ist ein grundlegendes Konzept in der Programmierung. Es ermöglicht es Ihrem Programm, mit externen Dateien wie Textdateien, CSV-Dateien und mehr zu interagieren. In Python ist eine der häufigsten Methoden, mit Dateien zu arbeiten, die Verwendung der `open()`-Funktion.

Die `open()`-Funktion wird in Python verwendet, um eine Datei zu öffnen. Sie nimmt zwei wichtige Argumente entgegen. Das erste Argument ist der Name der Datei, die Sie öffnen möchten. Das zweite Argument ist der Modus, in dem Sie die Datei öffnen möchten. Wenn Sie eine Datei lesen möchten, verwenden Sie den Modus 'r'. Dies teilt Python mit, dass Sie nur den Inhalt der Datei lesen und keine Änderungen daran vornehmen möchten.

Nun fügen wir dem `pcost.py`-File einige Codezeilen hinzu, um die `portfolio.dat`-Datei zu öffnen und zu lesen. Öffnen Sie die `pcost.py`-Datei in Ihrem Code-Editor und fügen Sie den folgenden Code hinzu:

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            print(line)  # Just for debugging, to see what we're reading

    # Return the total cost
    return total_cost

# Call the function with the portfolio file
total_cost = portfolio_cost('portfolio.dat')
print(f'Total cost: ${total_cost}')
```

Lassen Sie uns analysieren, was dieser Code tut:

1. Zunächst definieren wir eine Funktion namens `portfolio_cost()`. Diese Funktion nimmt einen Dateinamen als Eingabeparameter. Der Zweck dieser Funktion ist es, die Gesamtkosten eines Aktienportfolios basierend auf den Daten in der Datei zu berechnen.
2. Innerhalb der Funktion verwenden wir die `open()`-Funktion, um die angegebene Datei im Lesemodus zu öffnen. Die `with`-Anweisung wird hier verwendet, um sicherzustellen, dass die Datei ordnungsgemäß geschlossen wird, nachdem wir sie gelesen haben. Dies ist eine gute Praxis, um Ressourcenlecks zu vermeiden.
3. Anschließend verwenden wir eine `for`-Schleife, um die Datei zeilenweise zu lesen. Für jede Zeile in der Datei geben wir sie aus. Dies dient nur Debugging-Zwecken, damit wir sehen können, welche Daten wir aus der Datei lesen.
4. Nach dem Lesen der Datei gibt die Funktion die Gesamtkosten zurück. Derzeit ist die Gesamtkosten auf 0,0 gesetzt, da wir die eigentliche Berechnung noch nicht implementiert haben.
5. Außerhalb der Funktion rufen wir die `portfolio_cost()`-Funktion mit dem Dateinamen 'portfolio.dat' auf. Dies bedeutet, dass wir die Funktion bitten, die Gesamtkosten basierend auf den Daten in der `portfolio.dat`-Datei zu berechnen.
6. Schließlich geben wir die Gesamtkosten mit einem f-String aus.

Nun lassen wir diesen Code laufen, um zu sehen, was er tut. Sie können die Python-Datei aus dem Terminal mit dem folgenden Befehl ausführen:

```bash
python3 ~/project/pcost.py
```

Wenn Sie diesen Befehl ausführen, sollten Sie jede Zeile der `portfolio.dat`-Datei im Terminal sehen, gefolgt von den Gesamtkosten, die derzeit auf 0,0 gesetzt sind. Diese Ausgabe hilft Ihnen zu überprüfen, ob die Datei korrekt gelesen wird.
