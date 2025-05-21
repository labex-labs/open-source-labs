# Criando uma Função de Ordem Superior

Em Python, uma função de ordem superior é uma função que pode receber outra função como argumento. Isso permite maior flexibilidade e reutilização de código. Agora, vamos criar uma função de ordem superior chamada `convert_csv()`. Esta função lidará com as operações comuns de processamento de dados CSV, permitindo que você personalize como cada linha do CSV é convertida em um registro.

Abra o arquivo `reader.py` no WebIDE. Vamos adicionar uma função que receberá um iterável de dados CSV, uma função de conversão e, opcionalmente, cabeçalhos de coluna. A função de conversão será usada para transformar cada linha do CSV em um registro.

Aqui está o código para a função `convert_csv()`. Copie e cole-o em seu arquivo `reader.py`:

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function

    Args:
        lines: An iterable containing CSV data
        conversion_func: A function that takes headers and a row and returns a record
        headers: Column headers (optional). If None, the first row is used as headers

    Returns:
        A list of records as processed by conversion_func
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = conversion_func(headers, row)
        records.append(record)
    return records
```

Vamos detalhar o que essa função faz. Primeiro, ela inicializa uma lista vazia chamada `records` para armazenar os registros convertidos. Em seguida, ela usa a função `csv.reader()` para ler as linhas de dados CSV. Se nenhum cabeçalho for fornecido, ela pega a primeira linha como cabeçalhos. Para cada linha subsequente, ela aplica a `conversion_func` para converter a linha em um registro e adiciona-o à lista `records`. Finalmente, ela retorna a lista de registros.

Agora, precisamos de uma função de conversão simples para testar nossa função `convert_csv()`. Esta função receberá os cabeçalhos e uma linha e converterá a linha em um dicionário usando os cabeçalhos como chaves.

Aqui está o código para a função `make_dict()`. Adicione esta função ao seu arquivo `reader.py` também:

```python
def make_dict(headers, row):
    '''
    Convert a row to a dictionary using the provided headers
    '''
    return dict(zip(headers, row))
```

A função `make_dict()` usa a função `zip()` para emparelhar cada cabeçalho com seu valor correspondente na linha e, em seguida, cria um dicionário a partir desses pares.

Vamos testar essas funções. Abra um shell Python executando os seguintes comandos no terminal:

```bash
cd ~/project
python3 -i reader.py
```

A opção `-i` no comando `python3` inicia o interpretador Python em modo interativo e importa o arquivo `reader.py`, para que possamos usar as funções que acabamos de definir.

No shell Python, execute o seguinte código para testar nossas funções:

```python
# Open the CSV file
lines = open('portfolio.csv')

# Convert to a list of dictionaries using our new function
result = convert_csv(lines, make_dict)

# Print the result
print(result)
```

Este código abre o arquivo `portfolio.csv`, usa a função `convert_csv()` com a função de conversão `make_dict()` para converter os dados CSV em uma lista de dicionários e, em seguida, imprime o resultado.

Você deve ver uma saída semelhante à seguinte:

```
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

Esta saída mostra que nossa função de ordem superior `convert_csv()` funciona corretamente. Criamos com sucesso uma função que recebe outra função como argumento, o que nos dá a capacidade de alterar facilmente como os dados CSV são convertidos.

Para sair do shell Python, você pode digitar `exit()` ou pressionar Ctrl+D.
