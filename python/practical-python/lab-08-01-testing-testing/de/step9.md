# Übung 8.1: Schreiben von Unit-Tests

In einer separaten Datei `test_stock.py` schreiben Sie eine Reihe von Unit-Tests für die `Stock`-Klasse. Um Sie zu starten, hier ist ein kleiner Codeausschnitt, der die Instanzerstellung testet:

```python
# test_stock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

Führen Sie Ihre Unit-Tests aus. Sie sollten eine Ausgabe erhalten, die ungefähr so aussieht:

## .

Ran 1 tests in 0.000s

    OK

Wenn Sie sich vergewissert haben, dass es funktioniert, schreiben Sie zusätzliche Unit-Tests, die Folgendes überprüfen:

- Stellen Sie sicher, dass die `s.cost`-Eigenschaft den richtigen Wert (49010.0) zurückgibt.
- Stellen Sie sicher, dass die `s.sell()`-Methode richtig funktioniert. Sie sollte den Wert von `s.shares` entsprechend verringern.
- Stellen Sie sicher, dass das `s.shares`-Attribut nicht auf einen nicht ganzzahligen Wert gesetzt werden kann.

Für den letzten Teil müssen Sie überprüfen, dass eine Ausnahme ausgelöst wird. Ein einfacher Weg, das zu tun, ist mit Code wie diesem:

```python
class TestStock(unittest.TestCase):
 ...
    def test_bad_shares(self):
         s = stock.Stock('GOOG', 100, 490.1)
         with self.assertRaises(TypeError):
             s.shares = '100'
```
