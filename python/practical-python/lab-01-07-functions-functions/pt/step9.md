# Exercício 1.32: Usando uma função de biblioteca

Python vem com uma grande biblioteca padrão de funções úteis. Uma biblioteca que pode ser útil aqui é o módulo `csv`. Você deve usá-lo sempre que precisar trabalhar com arquivos de dados CSV. Aqui está um exemplo de como ele funciona:

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'shares', 'price']
>>> for row in rows:
        print(row)

['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
>>> f.close()
>>>
```

Uma coisa boa sobre o módulo `csv` é que ele lida com uma variedade de detalhes de baixo nível, como citação e divisão adequada por vírgulas. Na saída acima, você notará que ele removeu as aspas duplas dos nomes na primeira coluna.

Modifique seu programa `pcost.py` para que ele use o módulo `csv` para análise (parsing) e tente executar os exemplos anteriores.
