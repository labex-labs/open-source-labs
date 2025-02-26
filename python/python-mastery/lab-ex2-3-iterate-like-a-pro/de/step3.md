# Zählen mit enumerate()

`enumerate()` ist eine nützliche Funktion, wenn Sie während der Iteration einen Zähler oder Index beibehalten müssen. Beispielsweise möchten Sie annehmen, dass Sie eine zusätzliche Zeilennummer benötigen:

```python
>>> for rowno, row in enumerate(rows):
        print(rowno, row)

0 ['AA', '100', '32.20']
1 ['IBM', '50', '91.10']
2 ['CAT', '150', '83.44']
3 ['MSFT', '200', '51.23']
4 ['GE', '95', '40.37']
5 ['MSFT', '50', '65.10']
6 ['IBM', '100', '70.44']
>>>
```

Sie können dies mit der Entpackung kombinieren, wenn Sie auf die Struktur achten:

```python
>>> for rowno, (name, shares, price) in enumerate(rows):
        print(rowno, name, shares, price)

0 AA 100 32.20
1 IBM 50 91.10
2 CAT 150 83.44
3 MSFT 200 51.23
4 GE 95 40.37
5 MSFT 50 65.10
6 IBM 100 70.44
>>>
```
