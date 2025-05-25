# Exercício 3.7: Escolhendo um delimitador de coluna diferente

Embora os arquivos CSV sejam bastante comuns, também é possível que você encontre um arquivo que use um separador de coluna diferente, como uma tabulação ou espaço. Por exemplo, o arquivo `portfolio.dat` se parece com isto:

```csv
name shares price
"AA" 100 32.20
"IBM" 50 91.10
"CAT" 150 83.44
"MSFT" 200 51.23
"GE" 95 40.37
"MSFT" 50 65.10
"IBM" 100 70.44
```

A função `csv.reader()` permite que um delimitador de coluna diferente seja fornecido da seguinte forma:

```python
rows = csv.reader(f, delimiter=' ')
```

Modifique sua função `parse_csv()` em `/home/labex/project/fileparse_3.7.py` para que ela também permita que o delimitador seja alterado.

Por exemplo:

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.dat', types=[str, int, float], delimiter=' ')
>>> portfolio
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}, {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>>
```
