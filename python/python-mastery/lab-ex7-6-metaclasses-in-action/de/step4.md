# Testen unserer Implementierung

Nachdem wir unsere Metaklasse implementiert und die `Structure`-Klasse modifiziert haben, ist es Zeit, unsere Implementierung zu testen. Testing ist von entscheidender Bedeutung, da es uns hilft, sicherzustellen, dass alles korrekt funktioniert. Durch das Ausführen von Tests können wir potenzielle Probleme frühzeitig erkennen und sicherstellen, dass unser Code wie erwartet verhält.

Zunächst führen wir die Unit-Tests aus, um zu sehen, ob unsere `Stock`-Klasse wie erwartet funktioniert. Unit-Tests sind kleine, isolierte Tests, die einzelne Teile unseres Codes überprüfen. In diesem Fall möchten wir sicherstellen, dass die `Stock`-Klasse korrekt funktioniert. Um die Unit-Tests auszuführen, verwenden wir den folgenden Befehl im Terminal:

```bash
python3 teststock.py
```

Wenn alles korrekt funktioniert, sollten alle Tests ohne Fehler bestanden werden. Wenn die Tests erfolgreich ablaufen, sollte die Ausgabe in etwa so aussehen:

```
........
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

Die Punkte repräsentieren jeden Test, der bestanden wurde, und das abschließende `OK` gibt an, dass alle Tests erfolgreich waren.

Jetzt testen wir unsere `Stock`-Klasse mit einigen echten Daten und der Tabellenformatierungsfunktion. Dies gibt uns ein realitätsnäheres Szenario, um zu sehen, wie unsere `Stock`-Klasse mit Daten interagiert und wie die Tabellenformatierung funktioniert. Wir verwenden den folgenden Befehl im Terminal:

```bash
python3 -c "
from stock import Stock
from reader import read_csv_as_instances
from tableformat import create_formatter, print_table

# Read portfolio data into Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print('Portfolio:')
print(portfolio)

# Format and print the portfolio data
print('\nFormatted table:')
formatter = create_formatter('text')
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

In diesem Code importieren wir zunächst die erforderlichen Klassen und Funktionen. Dann lesen wir Daten aus einer CSV-Datei in `Stock`-Instanzen. Danach geben wir die Portfolio-Daten aus, formatieren sie in eine Tabelle und geben die formatierte Tabelle aus.

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Portfolio:
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]

Formatted table:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Nehmen Sie sich einen Moment Zeit, um zu würdigen, was wir erreicht haben:

1. Wir haben einen Mechanismus erstellt, um automatisch alle Validator-Typen zu sammeln. Das bedeutet, dass wir nicht manuell alle Validatoren verfolgen müssen, was uns Zeit spart und die Wahrscheinlichkeit von Fehlern verringert.
2. Wir haben eine Metaklasse implementiert, die diese Typen in den Namensraum von `Structure`-Unterklassen einfügt. Dies ermöglicht es den Unterklassen, diese Validatoren zu verwenden, ohne sie explizit importieren zu müssen.
3. Wir haben die Notwendigkeit für explizite Importe von Validator-Typen beseitigt. Dies macht unseren Code sauberer und leichter lesbar.
4. All dies geschieht im Hintergrund, wodurch der Code für die Definition neuer Strukturen sauber und einfach wird.

Die endgültige `stock.py`-Datei ist bemerkenswert sauber im Vergleich zu dem, was sie ohne unsere Metaklasse gewesen wäre:

```python
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Ohne die Notwendigkeit, die Validator-Typen direkt zu importieren, ist der Code kompakter und leichter zu warten. Dies ist ein großartiges Beispiel dafür, wie Metaklassen die Qualität unseres Codes verbessern können.
