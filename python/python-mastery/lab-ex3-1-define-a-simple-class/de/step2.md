# Lesen eines Portfolios aus einer CSV-Datei

In diesem Schritt werden wir eine Funktion erstellen, die Aktiendaten aus einer CSV-Datei liest und eine Liste von `Stock`-Objekten zurückgibt. Ein `Stock`-Objekt repräsentiert eine Aktienbesitzung, und am Ende dieses Schritts können Sie ein Portfolio von Aktien aus einer CSV-Datei lesen.

## Grundlegendes zu CSV-Dateien

CSV steht für Comma-Separated Values (Komma-separierte Werte) und ist ein sehr gängiges Format zum Speichern tabellarischer Daten. Stellen Sie sich eine CSV-Datei wie eine einfache Tabellenkalkulation vor. Jede Zeile in einer CSV-Datei repräsentiert eine Datenzeile, und die Spalten innerhalb dieser Zeile werden durch Kommas getrennt. Normalerweise enthält die erste Zeile einer CSV-Datei die Überschriften. Diese Überschriften beschreiben, welche Art von Daten in jeder Spalte enthalten sind. Beispielsweise könnten die Überschriften in einer CSV-Datei für ein Aktienportfolio "Name", "Anzahl" und "Preis" sein.

## Implementierungsanweisungen

1. Öffnen Sie zunächst die Datei `stock.py` in Ihrem Code-Editor. Wenn sie bereits geöffnet ist, ist das super! Wenn nicht, suchen Sie sie und öffnen Sie sie. Hier werden wir unsere neue Funktion hinzufügen.

2. Sobald die Datei `stock.py` geöffnet ist, suchen Sie nach dem Kommentar `# TODO: Add read_portfolio(filename) function here`. Dieser Kommentar ist ein Platzhalter, der uns sagt, wo wir unsere neue Funktion platzieren sollen.

3. Unterhalb dieses Kommentars fügen Sie die folgende Funktion hinzu. Diese Funktion heißt `read_portfolio` und nimmt einen Dateinamen als Argument entgegen. Der Zweck dieser Funktion besteht darin, die CSV-Datei zu lesen, die Aktiendaten zu extrahieren und eine Liste von `Stock`-Objekten zu erstellen.

```python
def read_portfolio(filename):
    """
    Read a CSV file containing portfolio data and return a list of Stock objects.

    Args:
        filename (str): Path to the CSV file

    Returns:
        list: A list of Stock objects
    """
    portfolio = []

    with open(filename, 'r') as f:
        headers = next(f).strip().split(',')  # Skip the header line

        for line in f:
            row = line.strip().split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])

            # Create a Stock object and add it to the portfolio list
            stock = Stock(name, shares, price)
            portfolio.append(stock)

    return portfolio
```

Lassen Sie uns analysieren, was diese Funktion tut. Zunächst erstellt sie eine leere Liste namens `portfolio`. Dann öffnet sie die CSV-Datei im Lesemodus. Die Anweisung `next(f)` überspringt die erste Zeile, die die Überschriftenzeile ist. Danach durchläuft sie jede Zeile in der Datei. Für jede Zeile teilt sie die Zeile in eine Liste von Werten auf, extrahiert den Namen, die Anzahl der Anteile und den Preis, erstellt ein `Stock`-Objekt und fügt es der `portfolio`-Liste hinzu. Schließlich gibt sie die `portfolio`-Liste zurück.

4. Nach dem Hinzufügen der Funktion speichern Sie die Datei `stock.py`. Sie können dies tun, indem Sie `Strg+S` auf Ihrer Tastatur drücken oder "Datei > Speichern" aus dem Menü in Ihrem Code-Editor auswählen. Das Speichern der Datei stellt sicher, dass Ihre Änderungen beibehalten werden.

5. Jetzt müssen wir unsere `read_portfolio`-Funktion testen. Erstellen Sie ein neues Python-Skript namens `test_portfolio.py`. Dieses Skript wird die `read_portfolio`-Funktion aus der Datei `stock.py` importieren, das Portfolio aus einer CSV-Datei lesen und Informationen über jede Aktie im Portfolio ausgeben.

```python
# test_portfolio.py
from stock import read_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print information about each stock
for stock in portfolio:
    print(f"Name: {stock.name}, Shares: {stock.shares}, Price: ${stock.price:.2f}")

# Print the total number of stocks in the portfolio
print(f"\nTotal number of stocks in portfolio: {len(portfolio)}")
```

In diesem Skript importieren wir zunächst die `read_portfolio`-Funktion. Dann rufen wir die Funktion mit dem Dateinamen `portfolio.csv` auf, um die Liste der `Stock`-Objekte zu erhalten. Danach durchlaufen wir die Liste und geben Informationen über jede Aktie aus. Schließlich geben wir die Gesamtanzahl der Aktien im Portfolio aus.

6. Um das Testskript auszuführen, öffnen Sie Ihr Terminal oder die Eingabeaufforderung, navigieren Sie zum Verzeichnis, in dem sich die Datei `test_portfolio.py` befindet, und führen Sie den folgenden Befehl aus:

```bash
python3 test_portfolio.py
```

Wenn alles korrekt funktioniert, sollten Sie eine Ausgabe sehen, die alle Aktien aus der Datei `portfolio.csv` auflistet, zusammen mit ihren Namen, der Anzahl der Anteile und den Preisen. Sie sollten auch die Gesamtanzahl der Aktien im Portfolio sehen.

```
Name: AA, Shares: 100, Price: $32.20
Name: IBM, Shares: 50, Price: $91.10
Name: CAT, Shares: 150, Price: $83.44
Name: MSFT, Shares: 200, Price: $51.23
Name: GE, Shares: 95, Price: $40.37
Name: MSFT, Shares: 50, Price: $65.10
Name: IBM, Shares: 100, Price: $00.44

Total number of stocks in portfolio: 7
```

Diese Ausgabe bestätigt, dass Ihre `read_portfolio`-Funktion die CSV-Datei korrekt liest und `Stock`-Objekte aus ihren Daten erstellt.
