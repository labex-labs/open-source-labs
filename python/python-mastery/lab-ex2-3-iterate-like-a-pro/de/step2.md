# Grundlegende Iteration und Entpackung

Die `for`-Anweisung iteriert über jede Sequenz von Daten. Beispielsweise:

```python
>>> for row in rows:
        print(row)

['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
>>>
```

Entpacken Sie die Werte in separate Variablen, wenn Sie dies benötigen:

```python
>>> for name, shares, price in rows:
        print(name, shares, price)

AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
>>>
```

Es ist eher üblich, `_` oder `__` als weggeworfene Variable zu verwenden, wenn Sie sich nicht um einen oder mehrere der Werte kümmern. Beispielsweise:

```python
>>> for name, _, price in rows:
        print(name, price)

AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
>>>
```

Wenn Sie nicht wissen, wie viele Werte entpackt werden, können Sie `*` als Platzhalter verwenden. Versuchen Sie dieses Experiment, um die Daten nach Namen zu gruppieren:

```python
>>> from collections import defaultdict
>>> byname = defaultdict(list)
>>> for name, *data in rows:
        byname[name].append(data)

>>> byname['IBM']
[['50', '91.10'], ['100', '70.44']]
>>> byname['CAT']
[['150', '83.44']]
>>> for shares, price in byname['IBM']:
        print(shares, price)

50 91.10
100 70.44
>>>
```
