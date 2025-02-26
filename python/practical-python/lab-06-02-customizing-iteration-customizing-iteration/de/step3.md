# Übung 6.4: Ein einfacher Generator

Wenn Sie jemals merken, dass Sie die Iteration anpassen möchten, sollten Sie immer an Generatorfunktionen denken. Sie sind einfach zu schreiben - erstellen Sie eine Funktion, die die gewünschte Iterationslogik ausführt, und verwenden Sie `yield`, um Werte auszugeben.

Beispielsweise versuchen Sie sich diesen Generator, der in einer Datei nach Zeilen mit einem passenden Substring sucht:

```python
>>> def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

>>> for line in open('portfolio.csv'):
        print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> for line in filematch('portfolio.csv', 'IBM'):
        print(line, end='')

"IBM",50,91.10
"IBM",100,70.44
>>>
```

Dies ist ziemlich interessant - die Idee, dass Sie eine Menge an benutzerdefiniertem Prozessieren in einer Funktion verstecken können und sie verwenden, um einer for-Schleife Werte zu liefern. Das nächste Beispiel betrachtet einen ungewöhnlicheren Fall.
