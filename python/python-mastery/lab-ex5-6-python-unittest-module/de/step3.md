# Unit-Tests mit erwarteten Fehlern

Angenommen, Sie möchten einen Unit-Test schreiben, der auf eine Ausnahme überprüft. Hier ist, wie Sie es tun können:

```python
class TestStock(unittest.TestCase):
 ...
    def test_bad_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
             s.shares = '50'
 ...
```

Verwenden Sie diesen Test als Leitfaden und schreiben Sie Unit-Tests für die folgenden Fehlerarten:

- Testen Sie, dass das Festlegen von `shares` auf einen String einen `TypeError` auslöst.
- Testen Sie, dass das Festlegen von `shares` auf eine negative Zahl einen `ValueError` auslöst.
- Testen Sie, dass das Festlegen von `price` auf einen String einen `TypeError` auslöst.
- Testen Sie, dass das Festlegen von `price` auf eine negative Zahl einen `ValueError` auslöst.
- Testen Sie, dass das Festlegen eines nicht vorhandenen Attributes `share` einen `AttributeError` auslöst.

Insgesamt sollten Sie ungefähr ein Dutzend Unit-Tests haben, wenn Sie fertig sind.

**Wichtige Bemerkung**

Für spätere Verwendung im Kurs sollten Sie eine voll funktionsfähige `stock.py`- und `teststock.py`-Datei haben. Speichern Sie Ihre Arbeit im Gange, wenn Sie müssen, aber Sie werden dringend dazu ermutigt, den Code aus `Lösungen/5_6` zu kopieren, wenn die Dinge noch nicht funktionieren.

Wir werden die `teststock.py`-Datei später als Werkzeug verwenden, um den `Stock`-Code zu verbessern. Sie sollten sie zur Hand haben, um sicherzustellen, dass der neue Code auf die gleiche Weise wie der alte Code funktioniert.
