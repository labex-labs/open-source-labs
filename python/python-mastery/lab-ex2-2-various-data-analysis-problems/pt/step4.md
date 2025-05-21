# Desafio de Análise de Dados com Dados da Chicago Transit Authority

Agora que você praticou o trabalho com diferentes estruturas de dados Python e o módulo collections, é hora de colocar essas habilidades em uso em uma tarefa de análise de dados do mundo real. Neste experimento, analisaremos os dados de passageiros de ônibus da Chicago Transit Authority (CTA). Essa aplicação prática o ajudará a entender como usar o Python para extrair informações significativas de conjuntos de dados do mundo real.

## Entendendo os Dados

Primeiro, vamos dar uma olhada nos dados de trânsito com os quais trabalharemos. Em seu terminal Python, você executará algum código para carregar os dados e entender sua estrutura básica.

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>> print(len(rows))
# This will show the number of records in the dataset

>>> # Let's look at the first record to understand the structure
>>> import pprint
>>> pprint.pprint(rows[0])
```

A instrução `import readrides` importa um módulo personalizado que possui uma função para ler os dados do arquivo CSV. A função `readrides.read_rides_as_dicts` lê os dados do arquivo CSV especificado e converte cada linha em um dicionário. `len(rows)` nos dá o número total de registros no conjunto de dados. Ao imprimir o primeiro registro usando `pprint.pprint(rows[0])`, podemos ver a estrutura de cada registro claramente.

Os dados contêm registros diários de passageiros para diferentes rotas de ônibus. Cada registro inclui:

- `route`: O número da rota do ônibus
- `date`: A data no formato "AAAA-MM-DD"
- `daytype`: "W" para dia de semana, "A" para sábado ou "U" para domingo/feriado
- `rides`: O número de passageiros naquele dia

## Tarefas de Análise

Vamos resolver cada uma das questões do desafio, uma por uma:

### Questão 1: Quantas rotas de ônibus existem em Chicago?

Para responder a esta pergunta, precisamos encontrar todos os números de rota exclusivos no conjunto de dados. Usaremos uma set comprehension para esta tarefa.

```python
>>> # Get all unique route numbers using a set comprehension
>>> unique_routes = {row['route'] for row in rows}
>>> print(len(unique_routes))
```

Uma set comprehension é uma maneira concisa de criar um conjunto. Neste caso, iteramos sobre cada linha na lista `rows` e extraímos o valor `route`. Como um conjunto armazena apenas elementos exclusivos, acabamos com um conjunto de todos os números de rota exclusivos. Imprimir o comprimento deste conjunto nos dá o número total de rotas de ônibus exclusivas.

Também podemos ver quais são algumas dessas rotas:

```python
>>> # Print a few of the route numbers
>>> print(list(unique_routes)[:10])
```

Aqui, convertemos o conjunto de rotas exclusivas em uma lista e, em seguida, imprimimos os primeiros 10 elementos dessa lista.

### Questão 2: Quantas pessoas andaram no ônibus número 22 em 2 de fevereiro de 2011?

Para esta pergunta, precisamos filtrar os dados para encontrar o registro específico que corresponde à rota e data fornecidas.

```python
>>> # Find rides on route 22 on February 2, 2011
>>> target_date = "2011-02-02"
>>> target_route = "22"
>>>
>>> for row in rows:
...     if row['route'] == target_route and row['date'] == target_date:
...         print(f"Rides on route {target_route} on {target_date}: {row['rides']}")
...         break
```

Primeiro, definimos as variáveis `target_date` e `target_route`. Em seguida, iteramos sobre cada linha na lista `rows`. Para cada linha, verificamos se a `route` e a `date` correspondem aos nossos valores de destino. Se uma correspondência for encontrada, imprimimos o número de viagens e saímos do loop, pois encontramos o registro que estamos procurando.

Você pode modificar isso para verificar qualquer rota em qualquer data, alterando as variáveis `target_date` e `target_route`.

### Questão 3: Qual é o número total de viagens feitas em cada rota de ônibus?

Vamos usar um Counter para calcular o total de viagens por rota. Um Counter é uma subclasse de dicionário do módulo `collections` que é usado para contar objetos hashable.

```python
>>> from collections import Counter
>>>
>>> # Initialize a counter
>>> total_rides_by_route = Counter()
>>>
>>> # Sum up rides for each route
>>> for row in rows:
...     total_rides_by_route[row['route']] += row['rides']
...
>>> # View the top 5 routes by total ridership
>>> for route, rides in total_rides_by_route.most_common(5):
...     print(f"Route {route}: {rides:,} total rides")
```

Primeiro, importamos a classe `Counter` do módulo `collections`. Em seguida, inicializamos um contador vazio chamado `total_rides_by_route`. Ao iterarmos sobre cada linha na lista `rows`, adicionamos o número de viagens para cada rota ao contador. Finalmente, usamos o método `most_common(5)` para obter as 5 principais rotas com o maior número total de passageiros e imprimir os resultados.

### Questão 4: Quais cinco rotas de ônibus tiveram o maior aumento de passageiros em dez anos, de 2001 a 2011?

Esta é uma tarefa mais complexa. Precisamos comparar o número de passageiros em 2001 com o de 2011 para cada rota.

```python
>>> # Create dictionaries to store total annual rides by route
>>> rides_2001 = Counter()
>>> rides_2011 = Counter()
>>>
>>> # Collect data for each year
>>> for row in rows:
...     if row['date'].startswith('2001-'):
...         rides_2001[row['route']] += row['rides']
...     elif row['date'].startswith('2011-'):
...         rides_2011[row['route']] += row['rides']
...
>>> # Calculate increases
>>> increases = {}
>>> for route in unique_routes:
...     if route in rides_2001 and route in rides_2011:
...         increase = rides_2011[route] - rides_2001[route]
...         increases[route] = increase
...
>>> # Find the top 5 routes with the biggest increases
>>> import heapq
>>> top_5_increases = heapq.nlargest(5, increases.items(), key=lambda x: x[1])
>>>
>>> # Display the results
>>> print("Top 5 routes with the greatest ridership increase from 2001 to 2011:")
>>> for route, increase in top_5_increases:
...     print(f"Route {route}: increased by {increase:,} rides")
...     print(f"  2001 rides: {rides_2001[route]:,}")
...     print(f"  2011 rides: {rides_2011[route]:,}")
...     print()
```

Primeiro, criamos dois objetos `Counter`, `rides_2001` e `rides_2011`, para armazenar o total de viagens para cada rota em 2001 e 2011, respectivamente. Ao iterarmos sobre cada linha na lista `rows`, verificamos se a data começa com '2001-' ou '2011-' e adicionamos as viagens ao contador apropriado.

Em seguida, criamos um dicionário vazio `increases` para armazenar o aumento no número de passageiros para cada rota. Iteramos sobre as rotas exclusivas e calculamos o aumento subtraindo as viagens de 2001 das viagens de 2011 para cada rota.

Para encontrar as 5 principais rotas com os maiores aumentos, usamos a função `heapq.nlargest`. Essa função recebe o número de elementos a serem retornados (5 neste caso), o iterável (`increases.items()`) e uma função de chave (`lambda x: x[1]`) que especifica como comparar os elementos.

Finalmente, imprimimos os resultados, mostrando o número da rota, o aumento no número de passageiros e o número de viagens em 2001 e 2011.

Esta análise identifica quais rotas de ônibus tiveram o maior crescimento no número de passageiros ao longo da década, o que pode indicar mudanças nos padrões populacionais, melhorias no serviço ou outras tendências interessantes.

Você pode estender essas análises de várias maneiras. Por exemplo, você pode querer:

- Analisar os padrões de passageiros por dia da semana
- Encontrar rotas com queda no número de passageiros
- Comparar as variações sazonais no número de passageiros

As técnicas que você aprendeu neste laboratório fornecem uma base sólida para esse tipo de exploração e análise de dados.
