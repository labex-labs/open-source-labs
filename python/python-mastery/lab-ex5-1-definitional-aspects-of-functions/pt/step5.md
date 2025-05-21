# Adicionando Dicas de Tipo

No Python 3.5 e versões posteriores, as dicas de tipo (type hints) são suportadas. As dicas de tipo são uma maneira de indicar os tipos de dados esperados de variáveis, parâmetros de função e valores de retorno em seu código. Elas não alteram como o código é executado, mas tornam o código mais legível e podem ajudar a detectar certos tipos de erros antes que o código seja realmente executado. Agora, vamos adicionar dicas de tipo às nossas funções de leitura CSV.

1. Abra o arquivo `reader.py` e atualize-o para incluir dicas de tipo:

```python
# reader.py

import csv
from typing import List, Callable, Dict, Any, Type, Optional, TextIO, Iterator, TypeVar

# Define a generic type for the class parameter
T = TypeVar('T')

def csv_as_dicts(lines: Iterator[str],
                types: List[Callable[[str], Any]],
                headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records: List[Dict[str, Any]] = []
    rows = csv.reader(lines)

    if headers is None:
        # Use the first row as headers if none provided
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: Iterator[str],
                    cls: Type[T],
                    headers: Optional[List[str]] = None) -> List[T]:
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV lines
    '''
    records: List[T] = []
    rows = csv.reader(lines)

    if headers is None:
        # Skip the first row if no headers provided
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename: str,
                     types: List[Callable[[str], Any]],
                     headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
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

def read_csv_as_instances(filename: str,
                         cls: Type[T],
                         headers: Optional[List[str]] = None) -> List[T]:
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

Vamos entender as principais mudanças que fizemos no código:

1. Importamos tipos do módulo `typing`. Este módulo fornece um conjunto de tipos que podemos usar para definir dicas de tipo. Por exemplo, `List`, `Dict` e `Optional` são tipos deste módulo.
2. Adicionamos uma variável de tipo genérico `T` para representar o tipo de classe. Uma variável de tipo genérico nos permite escrever funções que podem trabalhar com diferentes tipos de forma segura para tipos.
3. Adicionamos dicas de tipo a todos os parâmetros de função e valores de retorno. Isso deixa claro quais tipos de argumentos uma função espera e que tipo de valor ela retorna.
4. Usamos tipos de contêiner apropriados como `List`, `Dict` e `Optional`. `List` representa uma lista, `Dict` representa um dicionário e `Optional` indica que um parâmetro pode ter um determinado tipo ou ser `None`.
5. Usamos `Callable` para as funções de conversão de tipo. `Callable` é usado para indicar que um parâmetro é uma função que pode ser chamada.
6. Usamos o genérico `T` para expressar que `csv_as_instances` retorna uma lista de instâncias da classe passada. Isso ajuda a IDE e outras ferramentas a entender o tipo dos objetos retornados.

7. Agora, vamos criar um arquivo de teste simples para garantir que tudo ainda funcione corretamente:

```python
# test_types.py

import reader
import stock

# The functions should work exactly as before
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First item:", portfolio[0])

# But now we have better type checking and IDE support
stock_portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst stock:", stock_portfolio[0])

# We can see that stock_portfolio is a list of Stock objects
# This helps IDEs provide better code completion
first_stock = stock_portfolio[0]
print(f"\nName: {first_stock.name}")
print(f"Shares: {first_stock.shares}")
print(f"Price: {first_stock.price}")
print(f"Value: {first_stock.shares * first_stock.price}")
```

3. Execute o script de teste no terminal:

```bash
python test_types.py
```

A saída deve ser semelhante a:

```
First item: {'name': 'AA', 'shares': 100, 'price': 32.2}

First stock: Stock('AA', 100, 32.2)

Name: AA
Shares: 100
Price: 32.2
Value: 3220.0
```

As dicas de tipo não alteram como o código é executado, mas fornecem vários benefícios:

1. Elas oferecem melhor suporte de IDE com preenchimento de código. Quando você usa uma IDE como PyCharm ou VS Code, ela pode usar as dicas de tipo para sugerir os métodos e atributos corretos para suas variáveis.
2. Elas fornecem uma documentação mais clara sobre os tipos de parâmetros e retorno esperados. Apenas olhando para a definição da função, você pode dizer que tipos de argumentos ela espera e que tipo de valor ela retorna.
3. Elas permitem que você use verificadores de tipo estático como mypy para detectar erros antecipadamente. Os verificadores de tipo estático analisam seu código sem executá-lo e podem encontrar erros relacionados a tipos antes de você executar o código.
4. Elas melhoram a legibilidade e a capacidade de manutenção do código. Quando você ou outros desenvolvedores retornarem ao código mais tarde, será mais fácil entender o que o código está fazendo.

Em uma base de código grande, esses benefícios podem reduzir significativamente os bugs e tornar o código mais fácil de entender e manter.

**Observação:** As dicas de tipo são opcionais no Python, mas são cada vez mais usadas em código profissional. Bibliotecas como as da biblioteca padrão do Python e muitos pacotes de terceiros populares agora incluem dicas de tipo extensivas.
