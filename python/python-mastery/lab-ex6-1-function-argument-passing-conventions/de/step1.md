# Vorbereitung

Wir werden die `Stock`-Klasse von Grund auf neu erstellen, indem wir einige neue Techniken anwenden. Stellen Sie sicher, dass Sie Ihre Unit-Tests aus Übung 5.4 bequem zur Hand haben. Sie werden diese benötigen.

Wenn Sie eine Funktion definieren, wissen Sie wahrscheinlich bereits, dass Sie sie mit einer Kombination aus Positions- oder Schlüsselwortargumenten aufrufen können. Beispielsweise:

```python
>>> def foo(x, y, z):
        return x + y + z

>>> foo(1, 2, 3)
6
>>> foo(1, z=3, y=2)
6
>>>
```

Sie wissen auch möglicherweise, dass Sie Sequenzen und Wörterbücher als Funktionsargumente mit der \* und \*\* -Syntax übergeben können. Beispielsweise:

```python
>>> args = (1, 2, 3)
>>> foo(*args)
6
>>> kwargs = {'y':2, 'z':3 }
>>> foo(1,**kwargs)
6
>>>
```

Darüber hinaus können Sie Funktionen schreiben, die beliebig viele Positions- oder Schlüsselwortargumente akzeptieren, indem Sie die \* und \*\* -Syntax verwenden. Beispielsweise:

```python
>>> def foo(*args):
        print(args)

>>> foo(1,2)
(1, 2)
>>> foo(1,2,3,4,5)
(1, 2, 3, 4, 5)
>>> foo()
()
>>>
>>> def bar(**kwargs):
        print(kwargs)

>>> bar(x=1,y=2)
{'y': 2, 'x': 1}
>>> bar(x=1,y=2,z=3)
{'y': 2, 'x': 1, 'z': 3}
>>> bar()
{}
>>>
```

Variable Argumentfunktionen sind manchmal nützlich als Technik, um die Menge an Code zu reduzieren oder zu vereinfachen, den Sie tippen müssen. In dieser Übung werden wir diese Idee für einfache Datenstrukturen untersuchen.
