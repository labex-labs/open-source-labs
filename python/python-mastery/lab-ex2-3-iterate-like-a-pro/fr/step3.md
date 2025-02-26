# Compter avec enumerate()

`enumerate()` est une fonction utile si vous avez besoin de maintenir un compteur ou un index lors de l'itération. Par exemple, supposons que vous vouliez un numéro de ligne supplémentaire :

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

Vous pouvez combiner cela avec le déballage si vous êtes prudent quant à la manière dont vous structurez le code :

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
