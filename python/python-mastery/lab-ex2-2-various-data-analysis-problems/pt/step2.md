# Usando List, Set e Dictionary Comprehensions

As Python comprehensions são uma maneira realmente útil e concisa de criar novas coleções com base nas existentes. Coleções em Python podem ser listas, conjuntos ou dicionários, que são como contêineres que armazenam diferentes tipos de dados. Comprehensions permitem que você filtre certos dados, transforme os dados de alguma forma e os organize de forma mais eficiente. Nesta parte, usaremos nossos dados de portfólio para explorar como essas comprehensions funcionam.

Primeiro, você precisa abrir um terminal Python, assim como fez na etapa anterior. Depois que o terminal estiver aberto, você inserirá os seguintes exemplos um por um. Essa abordagem prática o ajudará a entender como as comprehensions funcionam na prática.

## List Comprehensions (Compreensões de Lista)

Uma list comprehension é uma sintaxe especial em Python que cria uma nova lista. Ele faz isso aplicando uma expressão a cada item em uma coleção existente.

Vamos começar com um exemplo. Primeiro, importaremos uma função para ler nossos dados de portfólio. Em seguida, usaremos a list comprehension para filtrar certas participações do portfólio.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

# Find all holdings with more than 100 shares
>>> large_holdings = [s for s in portfolio if s['shares'] > 100]
>>> print(large_holdings)
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

Neste código, primeiro importamos a função `read_portfolio` e a usamos para ler os dados do portfólio de um arquivo CSV. Em seguida, a list comprehension `[s for s in portfolio if s['shares'] > 100]` percorre cada item `s` na coleção `portfolio`. Ele inclui o item `s` na nova lista `large_holdings` somente se o número de ações nessa participação for maior que 100.

List comprehensions também podem ser usadas para realizar cálculos. Aqui estão alguns exemplos:

```python
# Calculate the total cost of each holding (shares * price)
>>> holding_costs = [s['shares'] * s['price'] for s in portfolio]
>>> print(holding_costs)
[3220.0, 4555.0, 12516.0, 10246.0, 3835.15, 3255.0, 7044.0]

# Calculate the total cost of the entire portfolio
>>> total_portfolio_cost = sum([s['shares'] * s['price'] for s in portfolio])
>>> print(total_portfolio_cost)
44671.15
```

No primeiro exemplo, a list comprehension `[s['shares'] * s['price'] for s in portfolio]` calcula o custo total de cada participação multiplicando o número de ações pelo preço de cada item no `portfolio`. No segundo exemplo, usamos a função `sum` junto com a list comprehension para calcular o custo total de todo o portfólio.

## Set Comprehensions (Compreensões de Conjunto)

Uma set comprehension é usada para criar um conjunto a partir de uma coleção existente. Um conjunto é uma coleção que contém apenas valores exclusivos.

Vamos ver como funciona com nossos dados de portfólio:

```python
# Find all unique stock names
>>> unique_stocks = {s['name'] for s in portfolio}
>>> print(unique_stocks)
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
```

Neste código, a set comprehension `{s['name'] for s in portfolio}` percorre cada item `s` no `portfolio` e adiciona o nome da ação (`s['name']`) ao conjunto `unique_stocks`. Como os conjuntos armazenam apenas valores exclusivos, acabamos com uma lista de todas as ações diferentes em nosso portfólio, sem quaisquer duplicatas.

## Dictionary Comprehensions (Compreensões de Dicionário)

Uma dictionary comprehension cria um novo dicionário aplicando expressões para criar pares chave-valor.

Aqui está um exemplo de como usar uma dictionary comprehension para contar o número total de ações para cada ação em nosso portfólio:

```python
# Create a dictionary to count total shares for each stock
>>> totals = {s['name']: 0 for s in portfolio}
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
```

Na primeira linha, a dictionary comprehension `{s['name']: 0 for s in portfolio}` cria um dicionário onde cada nome de ação (`s['name']`) é uma chave, e o valor inicial para cada chave é 0. Em seguida, usamos um loop `for` para percorrer cada item no `portfolio`. Para cada item, adicionamos o número de ações (`s['shares']`) ao valor correspondente no dicionário `totals`.

Essas comprehensions são muito poderosas porque permitem que você transforme e analise dados com apenas algumas linhas de código. Elas são uma ótima ferramenta para ter em seu kit de ferramentas de programação Python.
