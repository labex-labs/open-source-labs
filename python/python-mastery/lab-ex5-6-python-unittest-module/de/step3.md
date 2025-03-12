# Testen auf Ausnahmen

Das Testen ist ein entscheidender Teil der Softwareentwicklung, und ein wichtiger Aspekt davon ist es, sicherzustellen, dass Ihr Code Fehlerbedingungen richtig behandeln kann. In Python bietet das `unittest`-Modul eine bequeme Möglichkeit, zu testen, ob bestimmte Ausnahmen (Exceptions) wie erwartet ausgelöst werden.

1. Öffnen Sie die Datei `teststock.py`. Wir werden einige Testmethoden hinzufügen, die darauf ausgelegt sind, auf Ausnahmen zu prüfen. Diese Tests helfen uns, sicherzustellen, dass unser Code richtig reagiert, wenn er ungültige Eingaben erhält.

```python
def test_shares_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.shares = '50'

def test_shares_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.shares = -50

def test_price_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.price = '490.1'

def test_price_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.price = -490.1

def test_attribute_error(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(AttributeError):
        s.share = 100  # 'share' is incorrect, should be 'shares'
```

Jetzt verstehen wir, wie diese Ausnahmetests funktionieren.

- Die Anweisung `with self.assertRaises(ExceptionType):` erstellt einen Kontextmanager. Dieser Kontextmanager prüft, ob der Code innerhalb des `with`-Blocks die angegebene Ausnahme auslöst.
- Wenn die erwartete Ausnahme innerhalb des `with`-Blocks ausgelöst wird, besteht der Test. Dies bedeutet, dass unser Code die ungültige Eingabe richtig erkennt und die entsprechende Fehlermeldung auslöst.
- Wenn keine Ausnahme ausgelöst wird oder eine andere Ausnahme ausgelöst wird, scheitert der Test. Dies zeigt an, dass unser Code die ungültige Eingabe möglicherweise nicht wie erwartet behandelt.

Diese Tests sind darauf ausgelegt, die folgenden Szenarien zu überprüfen:

- Das Setzen des `shares`-Attributs auf eine Zeichenkette sollte einen `TypeError` auslösen, da `shares` eine Zahl sein sollte.
- Das Setzen des `shares`-Attributs auf eine negative Zahl sollte einen `ValueError` auslösen, da die Anzahl der Aktien nicht negativ sein kann.
- Das Setzen des `price`-Attributs auf eine Zeichenkette sollte einen `TypeError` auslösen, da `price` eine Zahl sein sollte.
- Das Setzen des `price`-Attributs auf eine negative Zahl sollte einen `ValueError` auslösen, da der Preis nicht negativ sein kann.
- Der Versuch, ein nicht existierendes Attribut `share` (beachten Sie das fehlende 's') zu setzen, sollte einen `AttributeError` auslösen, da der korrekte Attributname `shares` ist.

2. Nachdem Sie diese Testmethoden hinzugefügt haben, speichern Sie die Datei `teststock.py`. Führen Sie dann alle Tests aus, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:

```bash
python3 teststock.py
```

Wenn alles richtig funktioniert, sollten Sie eine Ausgabe sehen, die anzeigt, dass alle 12 Tests bestanden wurden. Die Ausgabe sieht wie folgt aus:

```
............
----------------------------------------------------------------------
Ran 12 tests in 0.002s

OK
```

Die zwölf Punkte repräsentieren alle Tests, die Sie bisher geschrieben haben. Es gab 7 Tests aus dem vorherigen Schritt, und wir haben gerade 5 neue hinzugefügt. Diese Ausgabe zeigt, dass Ihr Code Ausnahmen wie erwartet behandelt, was ein gutes Zeichen für ein gut getestetes Programm ist.
