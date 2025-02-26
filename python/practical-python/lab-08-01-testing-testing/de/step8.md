# Dritte-Party-Testwerkzeuge

Das integrierte `unittest`-Modul hat den Vorteil, überall verfügbar zu sein - es ist Teil von Python. Allerdings finden viele Programmierer auch, dass es ziemlich umständlich ist. Eine beliebte Alternative ist [pytest](https://docs.pytest.org/en/latest/). Mit pytest vereinfacht sich Ihre Testdatei zu etwas wie Folgendem:

```python
# test_simple.py
import simple

def test_simple():
    assert simple.add(2,2) == 4

def test_str():
    assert simple.add('hello','world') == 'helloworld'
```

Um einen Test auszuführen, geben Sie einfach einen Befehl wie `python -m pytest` ein. Es wird dann alle Tests finden und ausführen. Das Modul kann mit `pip install pytest` installiert werden.

Es gibt mit `pytest` viel mehr als dieses Beispiel, aber es ist normalerweise ziemlich einfach, loszulegen, sollten Sie sich entscheiden, es auszuprobieren.

In dieser Übung werden Sie die grundlegenden Mechanismen des Einsatzes des `unittest`-Moduls von Python erkunden.

In früheren Übungen haben Sie eine Datei `stock.py` geschrieben, die eine `Stock`-Klasse enthielt. Für diese Übung wird angenommen, dass Sie den in Übung 7.9 geschriebenen Code mit typisierten Eigenschaften verwenden. Wenn aus irgendeinem Grund das nicht funktioniert, können Sie die Lösung aus `Lösungen/7_9` in Ihr Arbeitsverzeichnis kopieren.
