# Es vernünftig gestalten

Das Verwenden von Mixins kann ein nützliches Werkzeug für Framework-Bauer sein, um die Menge an Code zu reduzieren, der geschrieben werden muss. Allerdings kann das Erfordern, dass Benutzer sich merken, wie man Klassen richtig zusammensetzt und Mehrfachvererbung verwendet, ihre Köpfe in Aufruhr setzen. In Übung 3.5 haben Sie eine Funktion `create_formatter()` geschrieben, die es einfacher macht, einen benutzerdefinierten Formatter zu erstellen. Nehmen Sie diese Funktion und erweitern Sie sie, um einige optionale Argumente zu verstehen, die mit den Mixin-Klassen zusammenhängen. Beispielsweise:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('csv', column_formats=['"%s"','%d','%0.2f'])
>>> print_table(portfolio, ['name','shares','price'], formatter)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44

>>> formatter = create_formatter('text', upper_headers=True)
>>> print_table(portfolio, ['name','shares','price'], formatter)
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

Im Hintergrund wird die Funktion `create_formatter()` die Klassen richtig zusammensetzen und eine passende `TableFormatter`-Instanz zurückgeben.
