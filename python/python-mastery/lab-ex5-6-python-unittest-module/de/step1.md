# Erstellen Ihres ersten Unit-Tests

Python's `unittest`-Modul ist ein leistungsstarkes Werkzeug, das eine strukturierte Möglichkeit bietet, Tests zu organisieren und auszuführen. Bevor wir uns mit dem Schreiben unseres ersten Unit-Tests befassen, sollten wir einige Schlüsselkonzepte verstehen. Test-Fixtures sind Methoden wie `setUp` und `tearDown`, die helfen, die Umgebung vor einem Test vorzubereiten und sie danach aufzuräumen. Testfälle sind einzelne Testeinheiten, Test-Suiten sind Sammlungen von Testfällen, und Test-Runner sind für die Ausführung dieser Tests und die Präsentation der Ergebnisse verantwortlich.

In diesem ersten Schritt werden wir eine grundlegende Testdatei für die `Stock`-Klasse erstellen, die bereits in der Datei `stock.py` definiert ist.

1. Zunächst öffnen wir die Datei `stock.py`. Dies hilft uns, die `Stock`-Klasse zu verstehen, die wir testen werden. Indem wir uns den Code in `stock.py` ansehen, können wir sehen, wie die Klasse strukturiert ist, welche Attribute sie hat und welche Methoden sie bereitstellt. Um den Inhalt der Datei `stock.py` anzuzeigen, führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
cat stock.py
```

2. Jetzt ist es an der Zeit, eine neue Datei mit dem Namen `teststock.py` mit Ihrem bevorzugten Texteditor zu erstellen. Diese Datei wird unsere Testfälle für die `Stock`-Klasse enthalten. Hier ist der Code, den Sie in der Datei `teststock.py` schreiben müssen:

```python
# teststock.py

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

Lassen Sie uns die Schlüsselkomponenten dieses Codes analysieren:

- `import unittest`: Diese Zeile importiert das `unittest`-Modul, das die notwendigen Werkzeuge und Klassen zum Schreiben und Ausführen von Tests in Python bereitstellt.
- `import stock`: Dies importiert das Modul, das unsere `Stock`-Klasse enthält. Ohne diesen Import könnten wir die `Stock`-Klasse in unserem Testcode nicht zugreifen.
- `class TestStock(unittest.TestCase)`: Wir erstellen eine neue Klasse namens `TestStock`, die von `unittest.TestCase` erbt. Dies macht unsere `TestStock`-Klasse zu einer Testfallklasse, die mehrere Testmethoden enthalten kann.
- `def test_create(self)`: Dies ist eine Testmethode. Im `unittest`-Framework müssen alle Testmethoden mit dem Präfix `test_` beginnen. Diese Methode erstellt eine Instanz der `Stock`-Klasse und verwendet dann die `assertEqual`-Methode, um zu überprüfen, ob die Attribute der `Stock`-Instanz den erwarteten Werten entsprechen.
- `assertEqual`: Dies ist eine Methode, die von der `TestCase`-Klasse bereitgestellt wird. Sie überprüft, ob zwei Werte gleich sind. Wenn sie nicht gleich sind, schlägt der Test fehl.
- `unittest.main()`: Wenn dieses Skript direkt ausgeführt wird, wird `unittest.main()` alle Testmethoden in der `TestStock`-Klasse ausführen und die Ergebnisse anzeigen.

3. Nachdem Sie den Code in der Datei `teststock.py` geschrieben haben, speichern Sie ihn. Führen Sie dann den folgenden Befehl in Ihrem Terminal aus, um den Test auszuführen:

```bash
python3 teststock.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

Der einzelne Punkt (`.`) in der Ausgabe gibt an, dass ein Test erfolgreich abgeschlossen wurde. Wenn ein Test fehlschlägt, sehen Sie anstelle des Punkts ein `F`, zusammen mit detaillierten Informationen darüber, was im Test schief gelaufen ist. Diese Ausgabe hilft Ihnen, schnell zu erkennen, ob Ihr Code wie erwartet funktioniert oder ob es Probleme gibt, die behoben werden müssen.
