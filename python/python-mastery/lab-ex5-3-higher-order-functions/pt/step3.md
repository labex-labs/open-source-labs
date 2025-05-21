# Refatorando Funções Existentes

Agora, criamos uma função de ordem superior chamada `convert_csv()`. Funções de ordem superior são funções que podem receber outras funções como argumentos ou retornar funções como resultados. Elas são um conceito poderoso em Python que pode nos ajudar a escrever um código mais modular e reutilizável. Nesta seção, usaremos essa função de ordem superior para refatorar as funções originais `csv_as_dicts()` e `csv_as_instances()`. Refatoração (Refactoring) é o processo de reestruturar o código existente sem alterar seu comportamento externo, visando melhorar sua estrutura interna, como eliminar a duplicação de código.

Vamos começar abrindo o arquivo `reader.py` no WebIDE. Atualizaremos as funções da seguinte forma:

1. Primeiro, substituiremos a função `csv_as_dicts()`. Esta função é usada para converter linhas de dados CSV em uma lista de dicionários. Aqui está o novo código:

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def dict_converter(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, dict_converter, headers=headers)
```

Neste código, definimos uma função interna `dict_converter` que recebe `headers` e `row` como argumentos. Ele usa uma compreensão de dicionário para criar um dicionário onde as chaves são os nomes dos cabeçalhos e os valores são o resultado da aplicação da função de conversão de tipo correspondente aos valores na linha. Em seguida, chamamos a função `convert_csv()` com a função `dict_converter` como argumento.

2. Em seguida, substituiremos a função `csv_as_instances()`. Esta função é usada para converter linhas de dados CSV em uma lista de instâncias de uma determinada classe. Aqui está o novo código:

```python
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    def instance_converter(headers, row):
        return cls.from_row(row)

    return convert_csv(lines, instance_converter, headers=headers)
```

Neste código, definimos uma função interna `instance_converter` que recebe `headers` e `row` como argumentos. Ele chama o método de classe `from_row` da classe `cls` fornecida para criar uma instância a partir da linha. Em seguida, chamamos a função `convert_csv()` com a função `instance_converter` como argumento.

Após refatorar essas funções, precisamos testá-las para garantir que ainda funcionem conforme o esperado. Para fazer isso, executaremos os seguintes comandos em um shell Python:

```bash
cd ~/project
python3 -i reader.py
```

O comando `cd ~/project` altera o diretório de trabalho atual para o diretório `project`. O comando `python3 -i reader.py` executa o arquivo `reader.py` em modo interativo, o que significa que podemos continuar a executar o código Python após a conclusão da execução do arquivo.

Depois que o shell Python estiver aberto, executaremos o seguinte código para testar as funções refatoradas:

```python
# Define a simple Stock class for testing
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

# Test csv_as_dicts
with open('portfolio.csv') as f:
    portfolio_dicts = csv_as_dicts(f, [str, int, float])
print("First dictionary:", portfolio_dicts[0])

# Test csv_as_instances
with open('portfolio.csv') as f:
    portfolio_instances = csv_as_instances(f, Stock)
print("First instance:", portfolio_instances[0])
```

Neste código, primeiro definimos uma classe `Stock` simples para teste. O método `__init__` inicializa os atributos de uma instância `Stock`. O método de classe `from_row` cria uma instância `Stock` a partir de uma linha de dados CSV. O método `__repr__` fornece uma representação de string da instância `Stock`.

Em seguida, testamos a função `csv_as_dicts()` abrindo o arquivo `portfolio.csv` e passando-o para a função junto com uma lista de funções de conversão de tipo. Imprimimos o primeiro dicionário na lista resultante.

Finalmente, testamos a função `csv_as_instances()` abrindo o arquivo `portfolio.csv` e passando-o para a função junto com a classe `Stock`. Imprimimos a primeira instância na lista resultante.

Se tudo estiver funcionando corretamente, você deverá ver uma saída semelhante à seguinte:

```
First dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
First instance: Stock(AA, 100, 32.2)
```

Esta saída indica que nossas funções refatoradas estão funcionando corretamente. Eliminamos com sucesso a duplicação de código, mantendo a mesma funcionalidade.

Para sair do shell Python, você pode digitar `exit()` ou pressionar Ctrl+D.
