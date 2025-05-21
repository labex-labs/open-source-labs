# Adicionando Verificação de Tipos a print_table()

Nesta etapa, vamos aprimorar a função `print_table()` no arquivo `tableformat.py`. Adicionaremos uma verificação para ver se o parâmetro `formatter` é uma instância válida de `TableFormatter`. Por que precisamos disso? Bem, a verificação de tipos é como uma rede de segurança para o seu código. Ela ajuda a garantir que os dados com os quais você está trabalhando sejam do tipo correto, o que pode evitar muitos bugs difíceis de encontrar.

## Compreendendo a Verificação de Tipos em Python

A verificação de tipos é uma técnica realmente útil na programação. Ela permite que você detecte erros no início do processo de desenvolvimento. Em Python, frequentemente lidamos com diferentes tipos de objetos, e às vezes esperamos que um determinado tipo de objeto seja passado para uma função. Para verificar se um objeto é de um tipo específico ou uma subclasse dele, podemos usar a função `isinstance()`. Por exemplo, se você tiver uma função que espera uma lista, pode usar `isinstance()` para garantir que a entrada seja de fato uma lista.

## Modificando a Função print_table()

Primeiro, abra o arquivo `tableformat.py` no seu editor de código. Role para baixo até o final do arquivo e você encontrará a função `print_table()`. Veja como ela se parece inicialmente:

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

Esta função recebe alguns dados, uma lista de colunas e um formatador. Em seguida, ela usa o formatador para imprimir uma tabela. Mas, no momento, ela não verifica se o formatador é do tipo correto.

Vamos modificá-la para adicionar a verificação de tipos. Usaremos a função `isinstance()` para verificar se o parâmetro `formatter` é uma instância de `TableFormatter`. Se não for, lançaremos um `TypeError` com uma mensagem clara. Aqui está o código modificado:

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

## Testando sua Implementação de Verificação de Tipos

Agora que adicionamos a verificação de tipos, precisamos garantir que ela funcione. Vamos criar um novo arquivo Python chamado `test_tableformat.py`. Aqui está o código que você deve colocar nele:

```python
import stock
import reader
import tableformat

# Read portfolio data
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Define a formatter that doesn't inherit from TableFormatter
class MyFormatter:
    def headings(self, headers):
        pass
    def row(self, rowdata):
        pass

# Try to use the non-compliant formatter
try:
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], MyFormatter())
    print("Test failed - type checking not implemented")
except TypeError as e:
    print(f"Test passed - caught error: {e}")
```

Neste código, primeiro lemos alguns dados de portfólio. Em seguida, definimos uma nova classe formatadora chamada `MyFormatter` que não herda de `TableFormatter`. Tentamos usar este formatador não compatível na função `print_table()`. Se nossa verificação de tipos estiver funcionando, ela deverá lançar um `TypeError`.

Para executar o teste, abra seu terminal e navegue até o diretório onde o arquivo `test_tableformat.py` está localizado. Em seguida, execute o seguinte comando:

```bash
python test_tableformat.py
```

Se tudo estiver funcionando corretamente, você deverá ver uma saída como esta:

```
Test passed - caught error: Expected a TableFormatter
```

Esta saída confirma que nossa verificação de tipos está funcionando como esperado. Agora, a função `print_table()` aceitará apenas um formatador que seja uma instância de `TableFormatter` ou uma de suas subclasses.
