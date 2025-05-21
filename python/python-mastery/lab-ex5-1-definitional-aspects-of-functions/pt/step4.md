# Lidando com Arquivos CSV Sem Cabeçalhos

No mundo do processamento de dados, nem todos os arquivos CSV vêm com cabeçalhos em sua primeira linha. Os cabeçalhos são os nomes dados a cada coluna em um arquivo CSV, que nos ajudam a entender que tipo de dados cada coluna contém. Quando um arquivo CSV não possui cabeçalhos, precisamos de uma maneira de lidar com ele adequadamente. Nesta seção, modificaremos nossas funções para permitir que o chamador forneça os cabeçalhos manualmente, para que possamos trabalhar com arquivos CSV com e sem cabeçalhos.

1. Abra o arquivo `reader.py` e atualize-o para incluir o tratamento de cabeçalhos:

```python
# reader.py

import csv

def csv_as_dicts(lines, types, headers=None):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # Use the first row as headers if none provided
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls, headers=None):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # Skip the first row if no headers provided
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers)

def read_csv_as_instances(filename, cls, headers=None):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers)
```

Vamos entender as principais mudanças que fizemos nessas funções:

1. Adicionamos um parâmetro `headers` a todas as funções e definimos seu valor padrão como `None`. Isso significa que, se o chamador não fornecer nenhum cabeçalho, as funções usarão o comportamento padrão.
2. Na função `csv_as_dicts`, usamos a primeira linha como cabeçalhos somente se o parâmetro `headers` for `None`. Isso nos permite lidar com arquivos com cabeçalhos automaticamente.
3. Na função `csv_as_instances`, ignoramos a primeira linha somente se o parâmetro `headers` for `None`. Isso ocorre porque, se estivermos fornecendo nossos próprios cabeçalhos, a primeira linha do arquivo são dados reais, não cabeçalhos.

4. Vamos testar essas modificações com nosso arquivo sem cabeçalhos. Crie um arquivo chamado `test_headers.py`:

```python
# test_headers.py

import reader
import stock

# Define column names for the file without headers
column_names = ['name', 'shares', 'price']

# Test reading a file without headers
portfolio = reader.read_csv_as_dicts('portfolio_noheader.csv',
                                     [str, int, float],
                                     headers=column_names)
print("First item from file without headers:", portfolio[0])
print("Total items:", len(portfolio))

# Test reading the same file as instances
portfolio = reader.read_csv_as_instances('portfolio_noheader.csv',
                                        stock.Stock,
                                        headers=column_names)
print("\nFirst item as Stock instance:", portfolio[0])
print("Total items:", len(portfolio))

# Verify that original functionality still works
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item from file with headers:", portfolio[0])
```

Neste script de teste, primeiro definimos os nomes das colunas para o arquivo sem cabeçalhos. Em seguida, testamos a leitura do arquivo sem cabeçalhos como uma lista de dicionários e como uma lista de instâncias de classe. Finalmente, verificamos se a funcionalidade original ainda funciona lendo um arquivo com cabeçalhos.

3. Execute o script de teste no terminal:

```bash
python test_headers.py
```

A saída deve ser semelhante a:

```
First item from file without headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7

First item from file with headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Essa saída confirma que nossas funções agora podem lidar com arquivos CSV com e sem cabeçalhos. O usuário pode fornecer nomes de colunas quando necessário ou confiar no comportamento padrão de leitura de cabeçalhos da primeira linha.

Ao fazer essa modificação, nossas funções de leitura CSV agora são mais versáteis e podem lidar com uma gama maior de formatos de arquivo. Esta é uma etapa importante para tornar nosso código mais robusto e útil em diferentes cenários.
