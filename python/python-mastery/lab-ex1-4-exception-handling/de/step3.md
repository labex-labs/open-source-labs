# Interaktive Experimente

Python bietet einen interaktiven Modus, der es Ihnen ermöglicht, Code sofort auszuführen. Dies ist super nützlich, um Ihren Code zu testen und neue Dinge auszuprobieren. In diesem Schritt lernen wir, wie man eine Funktion direkt aus dem Python-Interpreter aufruft.

## Ausführen von Python im interaktiven Modus

Um ein Python-Skript auszuführen und dann in den interaktiven Modus zu gelangen, können Sie die `-i`-Option verwenden. Diese Option teilt Python mit, nach der Ausführung des Skripts im interaktiven Zustand weiterzulaufen. So geht es:

```bash
cd /home/labex/project
python3 -i pcost.py
```

Lassen Sie uns analysieren, was dieser Befehl macht:

1. Zunächst wechselt `cd /home/labex/project` das aktuelle Verzeichnis zu `/home/labex/project`. Hier befindet sich unser `pcost.py`-Skript.
2. Dann führt `python3 -i pcost.py` das `pcost.py`-Skript aus. Nach Abschluss der Skriptausführung bleibt Python im interaktiven Modus.
3. Im interaktiven Modus können Sie direkt Python-Befehle in das Terminal eingeben.

Nachdem Sie den Befehl ausgeführt haben, sehen Sie die Ausgabe des `pcost.py`-Skripts, gefolgt vom Python-Prompt (`>>>`). Dieser Prompt zeigt an, dass Sie jetzt Python-Befehle eingeben können.

## Interaktives Aufrufen Ihrer Funktion

Sobald Sie sich im interaktiven Modus befinden, können Sie die `portfolio_cost()`-Funktion mit verschiedenen Dateinamen aufrufen. Dies ermöglicht es Ihnen, zu sehen, wie die Funktion mit verschiedenen Eingaben reagiert. Hier ist ein Beispiel:

```python
>>> portfolio_cost('/home/labex/project/portfolio.dat')
44671.15
>>> portfolio_cost('/home/labex/project/portfolio2.dat')
19908.75
>>> portfolio_cost('/home/labex/project/portfolio3.dat')
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

Mit diesem interaktiven Ansatz können Sie:

- Ihre Funktion mit verschiedenen Eingaben testen, um zu sehen, ob sie wie erwartet funktioniert.
- Die Funktionsweise der Funktion unter verschiedenen Bedingungen experimentell untersuchen.
- Ihren Code sofort debuggen, indem Sie die unmittelbaren Ergebnisse Ihrer Funktionsaufrufe sehen.

## Vorteile des interaktiven Modus

Der interaktive Modus hat mehrere Vorteile:

1. Sie können verschiedene Szenarien schnell testen, ohne jedes Mal das gesamte Skript ausführen zu müssen.
2. Sie können Variablen und Ausdrucksresultate sofort untersuchen, was Ihnen hilft, zu verstehen, was in Ihrem Code passiert.
3. Sie können kleine Code-Stücke testen, ohne ein vollständiges Programm zu erstellen. Dies ist ideal für das Lernen und Ausprobieren neuer Ideen.
4. Es ist eine ausgezeichnete Möglichkeit, Python zu lernen und zu experimentieren, da Sie sofortige Rückmeldung erhalten.

## Verlassen des interaktiven Modus

Wenn Sie mit Ihren Experimenten fertig sind, können Sie den interaktiven Modus auf zwei Arten verlassen:

- Geben Sie `exit()` ein und drücken Sie Enter. Dies ist eine einfache Möglichkeit, die interaktive Sitzung zu beenden.
- Drücken Sie Ctrl+D (unter Unix/Linux). Dies ist eine Tastenkombination, die ebenfalls den interaktiven Modus verlässt.

Im Laufe Ihrer Python-Programmierreise wird die Technik des Definierens von Funktionen und des interaktiven Testens äußerst wertvoll für die Entwicklung und das Debugging sein. Sie ermöglicht es Ihnen, schnell über Ihren Code zu iterieren und Probleme zu finden und zu beheben.
