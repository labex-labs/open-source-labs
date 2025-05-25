# Exercício 3.3: Lendo Arquivos CSV

Para começar, vamos apenas focar no problema de ler um arquivo CSV em uma lista de dicionários. No arquivo `fileparse_3.3.py`, defina uma função que se parece com isto:

```python
# fileparse_3.3.py
import csv

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

Esta função lê um arquivo CSV em uma lista de dicionários, enquanto esconde os detalhes de abertura do arquivo, envolvendo-o com o módulo `csv`, ignorando linhas em branco e assim por diante.

Experimente:

Dica: `python3 -i fileparse_3.3.py`.

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
>>>
```

Isso é bom, exceto que você não pode fazer nenhum tipo de cálculo útil com os dados porque tudo é representado como uma string. Vamos corrigir isso em breve, mas vamos continuar construindo sobre isso.
