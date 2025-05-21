# Explorando o Módulo Collections

Em Python, os contêineres embutidos, como listas, dicionários e conjuntos, são muito úteis. No entanto, o módulo `collections` do Python vai um passo além, fornecendo tipos de dados de contêiner especializados que estendem a funcionalidade desses contêineres embutidos. Vamos dar uma olhada mais de perto em alguns desses tipos de dados úteis.

Você continuará trabalhando em seu terminal Python e acompanhará os exemplos abaixo.

## Counter (Contador)

A classe `Counter` é uma subclasse do dicionário. Seu principal objetivo é contar objetos hashable (com hash). Ele oferece uma maneira conveniente de contar itens e suporta uma variedade de operações.

Primeiro, precisamos importar a classe `Counter` e uma função para ler um portfólio. Em seguida, leremos um portfólio de um arquivo CSV.

```python
>>> from collections import Counter
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

```

Agora, criaremos um objeto `Counter` para contar o número de ações para cada ação por seu nome.

```python
# Create a counter to count shares by stock name
>>> totals = Counter()
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
```

Uma das grandes características do objeto `Counter` é que ele inicializa automaticamente novas chaves com uma contagem de 0. Isso significa que você não precisa verificar se uma chave existe antes de incrementar sua contagem, o que simplifica o código para acumular contagens.

Os contadores também vêm com métodos especiais. Por exemplo, o método `most_common()` é muito útil para análise de dados.

```python
# Get the two stocks with the most shares
>>> most_common_stocks = totals.most_common(2)
>>> print(most_common_stocks)
[('MSFT', 250), ('IBM', 150)]
```

Além disso, os contadores podem ser combinados usando operações aritméticas.

```python
# Create another counter
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> print(more)
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})

# Add two counters together
>>> combined = totals + more
>>> print(combined)
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
```

## defaultdict (defaultdict)

O `defaultdict` é semelhante a um dicionário normal, mas tem um recurso exclusivo. Ele fornece um valor padrão para chaves que ainda não existem. Isso pode simplificar seu código, pois você não precisa mais verificar se uma chave existe antes de usá-la.

```python
>>> from collections import defaultdict

# Group portfolio entries by stock name
>>> byname = defaultdict(list)
>>> for s in portfolio:
...     byname[s['name']].append(s)
...
>>> print(byname['IBM'])
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> print(byname['AA'])
[{'name': 'AA', 'shares': 100, 'price': 32.2}]
```

Quando você cria um `defaultdict(list)`, ele cria automaticamente uma nova lista vazia para cada nova chave. Portanto, você pode anexar diretamente ao valor de uma chave, mesmo que a chave não existisse antes. Isso elimina a necessidade de verificar se a chave existe e criar uma lista vazia manualmente.

Você também pode usar outras funções de fábrica padrão. Por exemplo, você pode usar `int`, `float` ou até mesmo sua própria função personalizada.

```python
# Use defaultdict with int to count items
>>> word_counts = defaultdict(int)
>>> words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
>>> for word in words:
...     word_counts[word] += 1
...
>>> print(word_counts)
defaultdict(<class 'int'>, {'apple': 3, 'orange': 2, 'banana': 1})
```

Esses tipos de contêiner especializados do módulo `collections` podem tornar seu código mais conciso e eficiente quando você estiver trabalhando com dados.
