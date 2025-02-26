# Contando con enumerate()

`enumerate()` es una función útil si alguna vez necesita mantener un contador o índice mientras itera. Por ejemplo, suponga que desea un número de fila adicional:

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

Puede combinar esto con el desempaquetado si es cuidadoso con cómo estructura la información:

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
