# Das Erstellen Ihres eigenen Moduls

Nachdem Sie nun verstehen, wie Sie vorhandene Module nutzen können, ist es an der Zeit, ein neues Modul von Grund auf neu zu erstellen. Ein Modul in Python ist eine Datei, die Python-Definitionen und -Anweisungen enthält. Es ermöglicht Ihnen, Ihren Code in wiederverwendbare und verwaltbare Teile zu organisieren. Indem Sie Ihr eigenes Modul erstellen, können Sie verwandte Funktionen und Variablen zusammenfassen, wodurch Ihr Code modularer und leichter wartbar wird.

## Das Erstellen eines Berichtsmoduls

Erstellen wir ein einfaches Modul zur Generierung von Aktienberichten. Dieses Modul wird Funktionen haben, um eine Portfolio-Datei zu lesen und einen formatierten Bericht über die Aktien im Portfolio auszugeben.

1. Zunächst müssen wir eine neue Datei namens `report.py` erstellen. Dazu verwenden wir die Befehlszeile. Navigieren Sie in das `project`-Verzeichnis in Ihrem Home-Verzeichnis und erstellen Sie die Datei mit dem Befehl `touch`.

```bash
cd ~/project
touch report.py
```

2. Öffnen Sie nun die Datei `report.py` in Ihrem bevorzugten Texteditor und fügen Sie den folgenden Code hinzu. Dieser Code definiert zwei Funktionen und einen Hauptblock.

```python
# report.py

def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with
    keys: name, shares, price
    """
    portfolio = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                stock = {
                    'name': fields[0],
                    'shares': int(fields[1]),
                    'price': float(fields[2])
                }
                portfolio.append(stock)
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")
    return portfolio

def print_report(portfolio):
    """
    Print a report showing the stock name, shares, price, and total value
    """
    print("Name    Shares    Price    Value")
    print("-" * 40)
    total_value = 0.0
    for stock in portfolio:
        value = stock['shares'] * stock['price']
        total_value += value
        print(f"{stock['name']:6s} {stock['shares']:9d} {stock['price']:9.2f} {value:9.2f}")
    print("-" * 40)
    print(f"Total Value: {total_value:16.2f}")

if __name__ == "__main__":
    portfolio = read_portfolio('portfolio.dat')
    print_report(portfolio)
```

Die Funktion `read_portfolio` liest eine Datei mit Aktieninformationen und gibt eine Liste von Dictionaries zurück, wobei jedes Dictionary eine Aktie mit den Schlüsseln `name`, `shares` und `price` repräsentiert. Die Funktion `print_report` nimmt ein Portfolio (eine Liste von Aktien-Dictionaries) und gibt einen formatierten Bericht aus, der den Aktiennamen, die Anzahl der Anteile, den Preis und den Gesamtwert anzeigt. Der Hauptblock am Ende wird ausgeführt, wenn die Datei direkt ausgeführt wird. Er liest die Portfolio-Datei und gibt den Bericht aus.

3. Speichern Sie nach dem Hinzufügen des Codes die Datei und verlassen Sie den Editor.

## Das Testen Ihres Moduls

Testen wir unser neues Modul, um sicherzustellen, dass es wie erwartet funktioniert.

1. Zunächst führen wir das Skript direkt von der Befehlszeile aus. Dies führt den Hauptblock in der Datei `report.py` aus.

```bash
python3 report.py
```

Sie sollten einen formatierten Bericht sehen, der die Aktien im Portfolio und ihre Werte anzeigt. Dieser Bericht enthält den Aktiennamen, die Anzahl der Anteile, den Preis und den Gesamtwert, sowie den Gesamtwert des gesamten Portfolios.

```
Name    Shares    Price    Value
----------------------------------------
AA         100     32.20   3220.00
IBM         50     91.10   4555.00
CAT        150     83.44  12516.00
MSFT       200     51.23  10246.00
GE          95     40.37   3835.15
MSFT        50     65.10   3255.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         44671.15
```

2. Als Nächstes verwenden wir das Modul aus dem Python-Interpreter. Starten Sie den Python-Interpreter, indem Sie den Befehl `python3` im Terminal ausführen.

```bash
python3
```

Sobald der Interpreter läuft, können wir das `report`-Modul importieren und seine Funktionen nutzen.

```python
import report
portfolio = report.read_portfolio('portfolio.dat')
len(portfolio)  # Should return 7, the number of stocks
portfolio[0]    # First stock in the portfolio
```

Die Anweisung `import report` macht die in der Datei `report.py` definierten Funktionen und Variablen in der aktuellen Python-Sitzung verfügbar. Wir verwenden dann die Funktion `read_portfolio`, um die Portfolio-Datei zu lesen und das Ergebnis in der Variable `portfolio` zu speichern. Die Anweisung `len(portfolio)` gibt die Anzahl der Aktien im Portfolio zurück, und `portfolio[0]` gibt die erste Aktie im Portfolio zurück.

Sie sollten die folgende Ausgabe sehen:

```
7
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

3. Jetzt verwenden wir das importierte Modul, um die Gesamtkosten des Portfolios selbst zu berechnen. Wir gehen die Aktien im Portfolio durch und summieren den Gesamtwert jeder Aktie auf.

```python
total = 0.0
for stock in portfolio:
    total += stock['shares'] * stock['price']
print(total)
```

Die Ausgabe sollte `44671.15` sein, was dem Gesamtwert entspricht, der von der Funktion `print_report` ausgegeben wird.

4. Schließlich erstellen wir einen benutzerdefinierten Bericht für einen bestimmten Aktientyp. Wir filtern das Portfolio, um nur die IBM-Aktien einzuschließen, und verwenden dann die Funktion `print_report`, um einen Bericht für diese Aktien auszugeben.

```python
ibm_stocks = [stock for stock in portfolio if stock['name'] == 'IBM']
report.print_report(ibm_stocks)
```

Dies sollte einen Bericht ausgeben, der nur die IBM-Aktien und ihre Werte zeigt.

```
Name    Shares    Price    Value
----------------------------------------
IBM         50     91.10   4555.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         11599.00
```

5. Wenn Sie mit dem Testen fertig sind, beenden Sie den Python-Interpreter, indem Sie den Befehl `exit()` ausführen.

```python
exit()
```

Sie haben nun erfolgreich Ihr eigenes Python-Modul erstellt und verwendet, das sowohl Funktionen als auch einen Hauptblock kombiniert, der nur ausgeführt wird, wenn die Datei direkt ausgeführt wird. Dieser modulare Ansatz beim Programmieren ermöglicht es Ihnen, Code wiederzuverwenden und Ihre Projekte besser zu organisieren und zu warten.
