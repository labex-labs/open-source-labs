# Tornando as Funções Mais Flexíveis

Atualmente, nossas funções são limitadas à leitura de arquivos especificados por um nome de arquivo. Isso restringe sua usabilidade. Em programação, é frequentemente benéfico tornar as funções mais flexíveis para que possam lidar com diferentes tipos de entrada. Em nosso caso, seria ótimo se nossas funções pudessem trabalhar com qualquer iterável que produza linhas, como objetos de arquivo ou outras fontes. Dessa forma, podemos usar essas funções em mais cenários, como leitura de arquivos compactados ou outros fluxos de dados.

Vamos refatorar nosso código para permitir essa flexibilidade:

1. Abra o arquivo `reader.py`. Vamos modificá-lo para incluir algumas novas funções. Essas novas funções permitirão que nosso código trabalhe com diferentes tipos de iteráveis. Aqui está o código que você precisa adicionar:

```python
# reader.py

import csv

def csv_as_dicts(lines, types):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)
```

Vamos analisar mais de perto como refatoramos o código:

1. Criamos duas funções mais genéricas, `csv_as_dicts()` e `csv_as_instances()`. Essas funções são projetadas para trabalhar com qualquer iterável que produza linhas CSV. Isso significa que elas podem lidar com diferentes tipos de fontes de entrada, não apenas arquivos especificados por um nome de arquivo.
2. Reimplementamos `read_csv_as_dicts()` e `read_csv_as_instances()` para usar essas novas funções. Dessa forma, a funcionalidade original de leitura de um arquivo por nome de arquivo ainda está disponível, mas agora ela é construída sobre as funções mais flexíveis.
3. Essa abordagem mantém a compatibilidade com versões anteriores com o código existente. Isso significa que qualquer código que estava usando as funções antigas ainda funcionará conforme o esperado. Ao mesmo tempo, nossa biblioteca se torna mais flexível porque agora pode lidar com diferentes tipos de fontes de entrada.

4. Agora, vamos testar essas novas funções. Crie um arquivo chamado `test_reader_flexibility.py` e adicione o seguinte código a ele. Este código testará as novas funções com diferentes tipos de fontes de entrada:

```python
# test_reader_flexibility.py

import reader
import stock
import gzip

# Test opening a regular file
with open('portfolio.csv') as file:
    portfolio = reader.csv_as_dicts(file, [str, int, float])
    print("First item from open file:", portfolio[0])

# Test opening a gzipped file
with gzip.open('portfolio.csv.gz', 'rt') as file:  # 'rt' means read text
    portfolio = reader.csv_as_instances(file, stock.Stock)
    print("\nFirst item from gzipped file:", portfolio[0])

# Test backward compatibility
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item using backward compatible function:", portfolio[0])
```

3. Depois de criar o arquivo de teste, precisamos executar o script de teste no terminal. Abra seu terminal e navegue até o diretório onde o arquivo `test_reader_flexibility.py` está localizado. Em seguida, execute o seguinte comando:

```bash
python test_reader_flexibility.py
```

A saída deve ser semelhante a esta:

```
First item from open file: {'name': 'AA', 'shares': 100, 'price': 32.2}

First item from gzipped file: Stock('AA', 100, 32.2)

First item using backward compatible function: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Essa saída confirma que nossas funções agora funcionam com diferentes tipos de fontes de entrada, mantendo a compatibilidade com versões anteriores. As funções refatoradas podem processar dados de:

- Arquivos regulares abertos com `open()`
- Arquivos compactados abertos com `gzip.open()`
- Qualquer outro objeto iterável que produza linhas de texto

Isso torna nosso código muito mais flexível e fácil de usar em diferentes cenários.
