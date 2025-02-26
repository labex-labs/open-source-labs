# Übung 3.2: Erstellen einer obersten Ebene-Funktion für die Programmausführung

Nehmen Sie den letzten Teil Ihres Programms und verpacken Sie ihn in eine einzelne Funktion `portfolio_report(portfolio_filename, prices_filename)`. Stellen Sie sicher, dass die Funktion so funktioniert, dass der folgende Funktionsaufruf den Bericht wie zuvor erstellt:

```python
portfolio_report('/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv')
```

In dieser endgültigen Version wird Ihr Programm nichts weiter als eine Reihe von Funktionsdefinitionen sein, gefolgt von einem einzelnen Funktionsaufruf von `portfolio_report()` am Ende (der alle im Programm involvierten Schritte ausführt).

Indem Sie Ihr Programm in eine einzelne Funktion umwandeln, wird es einfacher, es mit unterschiedlichen Eingaben auszuführen. Versuchen Sie beispielsweise die folgenden Anweisungen interaktiv nach Ausführung Ihres Programms:

```python
>>> portfolio_report('/home/labex/project/portfolio2.csv', '/home/labex/project/prices.csv')
... schauen Sie sich die Ausgabe an...
>>> files = ['/home/labex/project/portfolio.csv', '/home/labex/project/portfolio2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, '/home/labex/project/prices.csv')
        print()

... schauen Sie sich die Ausgabe an...
>>>
```
