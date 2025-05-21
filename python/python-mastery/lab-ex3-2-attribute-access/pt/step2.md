# Usando `getattr()` para Processamento Genérico de Objetos

A função `getattr()` é uma ferramenta poderosa em Python que permite acessar atributos de um objeto de forma dinâmica. Isso é particularmente útil quando você deseja processar objetos de maneira genérica. Em vez de escrever código específico para um determinado tipo de objeto, você pode usar `getattr()` para trabalhar com qualquer objeto que tenha os atributos necessários. Essa flexibilidade torna seu código mais reutilizável e adaptável.

## Processando Múltiplos Atributos

Vamos começar aprendendo como acessar múltiplos atributos de um objeto usando a função `getattr()`. Este é um cenário comum quando você precisa extrair informações específicas de um objeto.

Primeiro, abra um shell interativo do Python se você fechou o anterior. Você pode fazer isso executando o seguinte comando em seu terminal:

```python
# Abra um shell interativo do Python se você fechou o anterior
python3
```

Em seguida, importaremos a classe `Stock` e criaremos um objeto `Stock`. A classe `Stock` representa uma ação com atributos como `name`, `shares` e `price`.

```python
# Importe a classe Stock e crie um objeto stock
from stock import Stock
s = Stock('GOOG', 100, 490.1)
```

Agora, definiremos uma lista de nomes de atributos que queremos acessar. Essa lista nos ajudará a iterar sobre os atributos e imprimir seus valores.

```python
# Defina uma lista de nomes de atributos
fields = ['name', 'shares', 'price']
```

Finalmente, usaremos um loop `for` para iterar sobre a lista de nomes de atributos e acessar cada atributo usando `getattr()`. Imprimiremos o nome do atributo e seu valor para cada iteração.

```python
# Acesse cada atributo usando getattr()
for name in fields:
    print(f"{name}: {getattr(s, 'name')}" if name == 'name' else f"{name}: {getattr(s, name)}")
```

Quando você executar este código, verá a seguinte saída:

```
name: GOOG
shares: 100
price: 490.1
```

Essa saída mostra que fomos capazes de acessar e imprimir os valores de múltiplos atributos do objeto `Stock` usando a função `getattr()`.

## Valores Padrão com getattr()

A função `getattr()` também fornece um recurso útil: a capacidade de especificar um valor padrão se o atributo que você está tentando acessar não existir. Isso pode impedir que seu código levante um `AttributeError` e torná-lo mais robusto.

Vamos ver como isso funciona. Primeiro, tentaremos acessar um atributo que não existe no objeto `Stock`. Usaremos `getattr()` e forneceremos um valor padrão de `'N/A'`.

```python
# Tente acessar um atributo que não existe
print(getattr(s, 'symbol', 'N/A'))  # Output: 'N/A'
```

Nesse caso, como o atributo `symbol` não existe no objeto `Stock`, `getattr()` retorna o valor padrão `'N/A'`.

Agora, vamos comparar isso com o acesso a um atributo existente. Acessaremos o atributo `name`, que existe no objeto `Stock`.

```python
# Compare com um atributo existente
print(getattr(s, 'name', 'N/A'))    # Output: 'GOOG'
```

Aqui, `getattr()` retorna o valor real do atributo `name`, que é `'GOOG'`.

## Processando uma Coleção de Objetos

A função `getattr()` torna-se ainda mais poderosa quando você precisa processar uma coleção de objetos. Vamos ver como podemos usá-la para processar uma carteira de ações.

Primeiro, importaremos a função `read_portfolio` do módulo `stock`. Essa função lê uma carteira de ações de um arquivo CSV e retorna uma lista de objetos `Stock`.

```python
# Importe a função de leitura da carteira
from stock import read_portfolio
```

Em seguida, usaremos a função `read_portfolio` para ler a carteira de um arquivo CSV chamado `portfolio.csv`.

```python
# Leia a carteira do arquivo CSV
portfolio = read_portfolio('portfolio.csv')
```

Finalmente, usaremos um loop `for` para iterar sobre a lista de objetos `Stock` na carteira. Para cada ação, usaremos `getattr()` para acessar os atributos `name` e `shares` e imprimir seus valores.

```python
# Imprima o nome e as ações de cada ação
for stock in portfolio:
    print(f"Stock: {getattr(stock, 'name')}, Shares: {getattr(stock, 'shares')}")
```

Essa abordagem torna seu código mais flexível porque você pode trabalhar com nomes de atributos como strings. Essas strings podem ser passadas como argumentos ou armazenadas em estruturas de dados, permitindo que você altere facilmente os atributos que deseja acessar sem modificar a lógica principal do seu código.
