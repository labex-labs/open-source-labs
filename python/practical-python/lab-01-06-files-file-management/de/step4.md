# Übung 1.26: Dateivorbereitungen

Zunächst versuchen Sie, die gesamte Datei als einen großen String auf einmal zu lesen:

```python
>>> with open('portfolio.csv', 'rt') as f:
        data = f.read()

>>> data
'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
>>> print(data)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>>
```

Im obigen Beispiel sollte bemerkt werden, dass Python zwei Ausgabemodi hat. Im ersten Modus, in dem Sie `data` an der Eingabeaufforderung eingeben, zeigt Ihnen Python die ursprüngliche Stringrepräsentation einschließlich von Anführungszeichen und Escapecodes. Wenn Sie `print(data)` eingeben, erhalten Sie die tatsächliche formatierte Ausgabe des Strings.

Obwohl das Lesen einer Datei auf einmal einfach ist, ist es oft nicht die am besten geeignete Methode, insbesondere wenn die Datei sehr groß ist oder Zeilen von Text enthält, die Sie zeilenweise verarbeiten möchten.

Um eine Datei zeilenweise zu lesen, verwenden Sie eine for-Schleife wie diese:

```python
>>> with open('portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
>>>
```

Wenn Sie diesen Code wie gezeigt verwenden, werden Zeilen gelesen, bis das Ende der Datei erreicht ist, an dem Punkt stoppt die Schleife.

In bestimmten Fällen möchten Sie möglicherweise manuell eine _einzige_ Zeile von Text lesen oder überspringen (z.B. möchten Sie vielleicht die erste Zeile der Spaltenüberschriften überspringen).

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f)
>>> headers
'name,shares,price\n'
>>> for line in f:
    print(line, end='')

"AA",100,32.20
"IBM",50,91.10
...
>>> f.close()
>>>
```

`next()` gibt die nächste Zeile von Text in der Datei zurück. Wenn Sie es wiederholt aufrufen würden, würden Sie aufeinanderfolgende Zeilen erhalten. Allerdings sollten Sie wissen, dass die for-Schleife bereits `next()` verwendet, um ihre Daten zu erhalten. Daher würden Sie es normalerweise nicht direkt aufrufen, es sei denn, Sie versuchen, wie gezeigt, explizit eine einzelne Zeile zu überspringen oder zu lesen.

Sobald Sie Zeilen einer Datei lesen, können Sie beginnen, weitere Verarbeitungen wie das Aufteilen durchzuführen. Beispielsweise versuchen Sie dies:

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f).split(',')
>>> headers
['name','shares', 'price\n']
>>> for line in f:
    row = line.split(',')
    print(row)

['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']
...
>>> f.close()
```

_Hinweis: In diesen Beispielen wird `f.close()` explizit aufgerufen, weil die `with`-Anweisung nicht verwendet wird._
