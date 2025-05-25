# Exercício 2.15: Um exemplo prático de `enumerate()`

Lembre-se que o arquivo `missing.csv` contém dados para uma carteira de ações, mas tem algumas linhas com dados ausentes. Usando `enumerate()`, modifique seu programa `pcost.py` para que ele imprima um número de linha com a mensagem de aviso quando encontrar uma entrada ruim.

```python
>>> cost = portfolio_cost('/home/labex/project/missing.csv')
Row 4: Couldn't convert: ['MSFT', '', '51.23']
Row 7: Couldn't convert: ['IBM', '', '70.44']
>>>
```

Para fazer isso, você precisará alterar algumas partes do seu código.

```python
...
for rowno, row in enumerate(rows, start=1):
    try:
        ...
    except ValueError:
        print(f'Row {rowno}: Bad row: {row}')
```
