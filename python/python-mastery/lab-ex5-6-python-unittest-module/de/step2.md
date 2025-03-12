# Erweitern Ihrer Testfälle

Nachdem Sie nun einen grundlegenden Testfall erstellt haben, ist es an der Zeit, Ihren Testumfang zu erweitern. Das Hinzufügen weiterer Tests hilft Ihnen, die restliche Funktionalität der `Stock`-Klasse abzudecken. Auf diese Weise können Sie sicherstellen, dass alle Aspekte der Klasse wie erwartet funktionieren. Wir werden die `TestStock`-Klasse ändern, um Tests für mehrere Methoden und Eigenschaften hinzuzufügen.

1. Öffnen Sie die Datei `teststock.py`. Innerhalb der `TestStock`-Klasse werden wir einige neue Testmethoden hinzufügen. Diese Methoden werden verschiedene Teile der `Stock`-Klasse testen. Hier ist der Code, den Sie hinzufügen müssen:

```python
def test_create_keyword_args(self):
    s = stock.Stock(name='GOOG', shares=100, price=490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_cost(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s.cost, 49010.0)

def test_sell(self):
    s = stock.Stock('GOOG', 100, 490.1)
    s.sell(20)
    self.assertEqual(s.shares, 80)

def test_from_row(self):
    row = ['GOOG', '100', '490.1']
    s = stock.Stock.from_row(row)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_repr(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

def test_eq(self):
    s1 = stock.Stock('GOOG', 100, 490.1)
    s2 = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s1, s2)
```

Schauen wir uns genauer an, was jeder dieser Tests tut:

- `test_create_keyword_args`: Dieser Test prüft, ob Sie ein `Stock`-Objekt mithilfe von Schlüsselwortargumenten erstellen können. Er überprüft, ob die Attribute des Objekts korrekt gesetzt sind.
- `test_cost`: Dieser Test prüft, ob die `cost`-Eigenschaft eines `Stock`-Objekts den korrekten Wert zurückgibt, der als Anzahl der Aktien multipliziert mit dem Preis berechnet wird.
- `test_sell`: Dieser Test prüft, ob die `sell()`-Methode eines `Stock`-Objekts die Anzahl der Aktien korrekt aktualisiert, nachdem einige verkauft wurden.
- `test_from_row`: Dieser Test prüft, ob die Klassenmethode `from_row()` eine neue `Stock`-Instanz aus einer Datenzeile erstellen kann.
- `test_repr`: Dieser Test prüft, ob die `__repr__()`-Methode eines `Stock`-Objekts die erwartete Zeichenkettenrepräsentation zurückgibt.
- `test_eq`: Dieser Test prüft, ob die `__eq__()`-Methode zwei `Stock`-Objekte korrekt vergleicht, um festzustellen, ob sie gleich sind.

2. Nachdem Sie diese Testmethoden hinzugefügt haben, speichern Sie die Datei `teststock.py`. Führen Sie dann die Tests erneut aus, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:

```bash
python3 teststock.py
```

Wenn alle Tests erfolgreich sind, sollten Sie eine Ausgabe wie diese sehen:

```
......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

Die sieben Punkte in der Ausgabe repräsentieren jeden Test. Jeder Punkt gibt an, dass ein Test erfolgreich abgeschlossen wurde. Wenn Sie also sieben Punkte sehen, bedeutet dies, dass alle sieben Tests bestanden wurden.
