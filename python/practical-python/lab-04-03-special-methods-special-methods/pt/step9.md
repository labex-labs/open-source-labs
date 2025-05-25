# Exercício 4.10: Um exemplo de uso de `getattr()`

`getattr()` é um mecanismo alternativo para ler atributos. Ele pode ser usado para escrever código extremamente flexível. Para começar, experimente este exemplo:

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.1)
>>> columns = ['name', 'shares']
>>> for colname in columns:
        print(colname, '=', getattr(s, colname))

name = GOOG
shares = 100
>>>
```

Observe cuidadosamente que os dados de saída são determinados inteiramente pelos nomes dos atributos listados na variável `columns`.

No arquivo `tableformat.py`, use essa ideia e expanda-a em uma função generalizada `print_table()` que imprime uma tabela mostrando atributos especificados pelo usuário de uma lista de objetos arbitrários. Assim como com a função `print_report()` anterior, `print_table()` também deve aceitar uma instância de `TableFormatter` para controlar o formato de saída. Veja como deve funcionar:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('txt')
>>> print_table(portfolio, ['name','shares'], formatter)
      name     shares
---------- ----------
        AA        100
       IBM         50
       CAT        150
      MSFT        200
        GE         95
      MSFT         50
       IBM        100

>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
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
