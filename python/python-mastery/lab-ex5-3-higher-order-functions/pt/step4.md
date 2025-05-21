# Usando a Função `map()`

Em Python, uma função de ordem superior é uma função que pode receber outra função como argumento ou retornar uma função como resultado. A função `map()` do Python é um ótimo exemplo de uma função de ordem superior. É uma ferramenta poderosa que permite aplicar uma determinada função a cada item em um iterável, como uma lista ou uma tupla. Após aplicar a função a cada item, ela retorna um iterador dos resultados. Esse recurso torna `map()` perfeito para processar sequências de dados, como linhas em um arquivo CSV.

A sintaxe básica da função `map()` é a seguinte:

```python
map(function, iterable, ...)
```

Aqui, a `function` é a operação que você deseja realizar em cada item no `iterable`. O `iterable` é uma sequência de itens, como uma lista ou uma tupla.

Vamos analisar um exemplo simples. Suponha que você tenha uma lista de números e queira elevar ao quadrado cada número dessa lista. Você pode usar a função `map()` para conseguir isso. Veja como você pode fazer:

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

Neste exemplo, primeiro definimos uma lista chamada `numbers`. Em seguida, usamos a função `map()`. A função `lambda` `lambda x: x * x` é a operação que queremos realizar em cada item na lista `numbers`. A função `map()` aplica essa função `lambda` a cada número na lista. Como `map()` retorna um iterador, convertemos para uma lista usando a função `list()`. Finalmente, imprimimos a lista `squared`, que contém os valores ao quadrado dos números originais.

Agora, vamos dar uma olhada em como podemos usar a função `map()` para modificar nossa função `convert_csv()`. Anteriormente, usamos um loop `for` para iterar sobre as linhas nos dados CSV. Agora, substituiremos esse loop `for` pela função `map()`.

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    # Use map to apply conversion_func to each row
    records = list(map(lambda row: conversion_func(headers, row), rows))
    return records
```

Esta versão atualizada da função `convert_csv()` faz exatamente a mesma coisa que a versão anterior, mas usa a função `map()` em vez de um loop `for`. A função `lambda` dentro de `map()` pega cada linha dos dados CSV e aplica a `conversion_func` a ela, junto com os cabeçalhos.

Vamos testar esta função atualizada para garantir que ela funcione corretamente. Primeiro, abra seu terminal e navegue até o diretório do projeto. Em seguida, inicie o shell interativo do Python com o arquivo `reader.py`.

```bash
cd ~/project
python3 -i reader.py
```

Depois de entrar no shell Python, execute o seguinte código para testar a função `convert_csv()` atualizada:

```python
# Test the updated convert_csv function
with open('portfolio.csv') as f:
    result = convert_csv(f, make_dict)
print(result[0])  # Should print the first dictionary

# Test that csv_as_dicts still works
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # Should print the first dictionary with converted types
```

Após executar este código, você deverá ver uma saída semelhante à seguinte:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Esta saída mostra que a função `convert_csv()` atualizada usando a função `map()` funciona corretamente, e as funções que dependem dela também continuam funcionando como esperado.

Usar a função `map()` tem várias vantagens:

1. Pode ser mais conciso do que um loop `for`. Em vez de escrever várias linhas de código para um loop `for`, você pode obter o mesmo resultado com uma única linha usando `map()`.
2. Comunica claramente sua intenção de transformar cada item em uma sequência. Quando você vê `map()`, você sabe imediatamente que está aplicando uma função a cada item em um iterável.
3. Pode ser mais eficiente em termos de memória porque retorna um iterador. Um iterador gera valores sob demanda, o que significa que não armazena todos os resultados na memória de uma vez. Em nosso exemplo, convertemos o iterador retornado por `map()` em uma lista, mas em alguns casos, você pode trabalhar diretamente com o iterador para economizar memória.

Para sair do shell Python, você pode digitar `exit()` ou pressionar Ctrl+D.
