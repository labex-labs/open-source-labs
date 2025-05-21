# Criando as Funções Básicas do Leitor CSV

Vamos começar criando um arquivo `reader.py` com duas funções básicas para ler dados CSV. Essas funções nos ajudarão a lidar com arquivos CSV de diferentes maneiras, como converter os dados em dicionários ou instâncias de classe.

Primeiro, precisamos entender o que é um arquivo CSV. CSV significa _Comma-Separated Values_ (Valores Separados por Vírgula). É um formato de arquivo simples usado para armazenar dados tabulares, onde cada linha representa uma linha e os valores em cada linha são separados por vírgulas.

Agora, vamos criar o arquivo `reader.py`. Siga estas etapas:

1. Abra o editor de código e crie um novo arquivo chamado `reader.py` no diretório `/home/labex/project`. É aqui que escreveremos nossas funções para ler dados CSV.

2. Adicione o seguinte código a `reader.py`:

```python
# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

Na função `read_csv_as_dicts`, primeiro abrimos o arquivo CSV usando a função `open`. Em seguida, usamos `csv.reader` para ler o arquivo linha por linha. A instrução `next(rows)` lê a primeira linha do arquivo, que geralmente contém os cabeçalhos. Depois disso, iteramos sobre as linhas restantes. Para cada linha, criamos um dicionário onde as chaves são os cabeçalhos e os valores são os valores correspondentes na linha, com conversão de tipo opcional usando a lista `types`.

A função `read_csv_as_instances` é semelhante, mas em vez de criar dicionários, ela cria instâncias de uma determinada classe. Ela assume que a classe tem um método estático chamado `from_row` que pode criar uma instância a partir de uma linha de dados.

3. Vamos testar essas funções para garantir que elas funcionem corretamente. Crie um novo arquivo chamado `test_reader.py` com o seguinte código:

```python
# test_reader.py

import reader
import stock

# Test reading CSV as dictionaries
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First portfolio item as dictionary:", portfolio_dicts[0])
print("Total items:", len(portfolio_dicts))

# Test reading CSV as class instances
portfolio_instances = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst portfolio item as Stock instance:", portfolio_instances[0])
print("Total items:", len(portfolio_instances))
```

No arquivo `test_reader.py`, importamos o módulo `reader` que acabamos de criar e o módulo `stock`. Em seguida, testamos as duas funções chamando-as com um arquivo CSV de amostra chamado `portfolio.csv`. Imprimimos o primeiro item e o número total de itens no portfólio para verificar se as funções estão funcionando conforme o esperado.

4. Execute o script de teste no terminal:

```bash
python test_reader.py
```

A saída deve ser semelhante a esta:

```
First portfolio item as dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First portfolio item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7
```

Isso confirma que nossas duas funções estão funcionando corretamente. A primeira função converte dados CSV em uma lista de dicionários com a conversão de tipo adequada, e a segunda função cria instâncias de classe usando um método estático na classe fornecida.

Na próxima etapa, vamos refatorar essas funções para torná-las mais flexíveis, permitindo que elas funcionem com qualquer fonte de dados iterável, e não apenas com nomes de arquivos.
