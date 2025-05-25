# Exercício 3.4: Construindo um Seletor de Colunas

Em muitos casos, você está interessado apenas em colunas selecionadas de um arquivo CSV, não em todos os dados. Modifique a função `parse_csv()` para que ela permita opcionalmente que colunas especificadas pelo usuário sejam selecionadas da seguinte forma:

```python
>>> # Read all of the data
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]

>>> # Read only some of the data
>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares'])
>>> shares_held
[{'name': 'AA', 'shares': '100'}, {'name': 'IBM', 'shares': '50'}, {'name': 'CAT', 'shares': '150'}, {'name': 'MSFT', 'shares': '200'}, {'name': 'GE', 'shares': '95'}, {'name': 'MSFT', 'shares': '50'}, {'name': 'IBM', 'shares': '100'}]
>>>
```

Um exemplo de um seletor de coluna foi dado no Exercício 2.23. No entanto, aqui está uma maneira de fazê-lo:

```python
# fileparse_3.4.py
import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]

            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

Há uma série de partes complicadas nesta parte. Provavelmente a mais importante é o mapeamento das seleções de coluna para os índices de linha. Por exemplo, suponha que o arquivo de entrada tenha os seguintes cabeçalhos:

```python
>>> headers = ['name', 'date', 'time', 'shares', 'price']
>>>
```

Agora, suponha que as colunas selecionadas fossem as seguintes:

```python
>>> select = ['name', 'shares']
>>>
```

Para realizar a seleção adequada, você precisa mapear os nomes das colunas selecionadas para os índices das colunas no arquivo. É isso que esta etapa está fazendo:

```python
>>> indices = [headers.index(colname) for colname in select ]
>>> indices
[0, 3]
>>>
```

Em outras palavras, "name" é a coluna 0 e "shares" é a coluna 3. Quando você lê uma linha de dados do arquivo, os índices são usados para filtrá-la:

```python
>>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['AA', '100']
>>>
```
