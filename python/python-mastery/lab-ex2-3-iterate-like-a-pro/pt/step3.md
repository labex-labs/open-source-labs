# Expressões Geradoras e Eficiência de Memória

Nesta etapa, vamos explorar as expressões geradoras. Elas são incrivelmente úteis quando você está lidando com grandes conjuntos de dados em Python. Elas podem tornar seu código muito mais eficiente em termos de memória, o que é crucial quando você está trabalhando com uma grande quantidade de dados.

## Compreendendo as Expressões Geradoras

Uma expressão geradora é semelhante a uma list comprehension, mas há uma diferença fundamental. Quando você usa uma list comprehension, o Python cria uma lista com todos os resultados de uma vez. Isso pode consumir muita memória, especialmente se você estiver trabalhando com um grande conjunto de dados. Por outro lado, uma expressão geradora produz resultados um de cada vez, conforme necessário. Isso significa que ela não precisa armazenar todos os resultados na memória de uma vez, o que pode economizar uma quantidade significativa de memória.

Vamos analisar um exemplo simples para ver como isso funciona:

```python
# Inicie uma nova sessão Python, se necessário
# python3

# List comprehension (cria uma lista na memória)
nums = [1, 2, 3, 4, 5]
squares_list = [x*x for x in nums]
print(squares_list)

# Expressão geradora (cria um objeto gerador)
squares_gen = (x*x for x in nums)
print(squares_gen)  # Isso não imprime os valores, apenas o objeto gerador

# Itere pelo gerador para obter valores
for n in squares_gen:
    print(n)
```

Quando você executa este código, verá a seguinte saída:

```
[1, 4, 9, 16, 25]
<generator object <genexpr> at 0x7f...>
1
4
9
16
25
```

Uma coisa importante a observar sobre os geradores é que eles só podem ser iterados uma vez. Depois de percorrer todos os valores em um gerador, ele é esgotado e você não pode obter os valores novamente.

```python
# Tente iterar novamente sobre o mesmo gerador
for n in squares_gen:
    print(n)  # Nada será impresso, pois o gerador já está esgotado
```

Você também pode obter valores manualmente de um gerador, um de cada vez, usando a função `next()`.

```python
# Crie um novo gerador
squares_gen = (x*x for x in nums)

# Obtenha valores um por um
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4
print(next(squares_gen))  # 9
```

Quando não houver mais valores no gerador, chamar `next()` levantará uma exceção `StopIteration`.

## Funções Geradoras com yield

Para uma lógica de gerador mais complexa, você pode escrever funções geradoras usando a instrução `yield`. Uma função geradora é um tipo especial de função que usa `yield` para retornar valores um de cada vez, em vez de retornar um único resultado de uma vez.

```python
def squares(nums):
    for x in nums:
        yield x*x

# Use a função geradora
for n in squares(nums):
    print(n)
```

Quando você executa este código, verá a seguinte saída:

```
1
4
9
16
25
```

## Reduzindo o Uso de Memória com Expressões Geradoras

Agora, vamos ver como as expressões geradoras podem economizar memória ao trabalhar com grandes conjuntos de dados. Usaremos o arquivo de dados do ônibus CTA, que é bastante grande.

```bash
cd /home/labex/project
unzip ctabus.csv.zip && rm ctabus.csv.zip
```

Primeiro, vamos tentar uma abordagem intensiva em memória:

```python
import tracemalloc
tracemalloc.start()

import readrides
rows = readrides.read_rides_as_dicts('ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Verifique o uso de memória
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

Agora, saia do Python e reinicie-o para comparar com uma abordagem baseada em geradores:

```bash
exit() python3
```

```python
import tracemalloc
tracemalloc.start()

import csv
f = open('ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)

# Use expressões geradoras para todas as operações
rows = (dict(zip(headers, row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Verifique o uso de memória
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

Você deve notar uma diferença significativa no uso de memória entre essas duas abordagens. A abordagem baseada em geradores processa os dados incrementalmente, sem carregar tudo na memória de uma vez, o que é muito mais eficiente em termos de memória.

## Expressões Geradoras com Funções de Redução

As expressões geradoras são particularmente úteis quando combinadas com funções como `sum()`, `min()`, `max()`, `any()` e `all()` que processam uma sequência inteira e produzem um único resultado.

Vamos analisar alguns exemplos:

```python
from readport import read_portfolio
portfolio = read_portfolio('portfolio.csv')

# Calcule o valor total da carteira
total_value = sum(s['shares']*s['price'] for s in portfolio)
print(f"Total portfolio value: {total_value}")

# Encontre o número mínimo de ações em qualquer participação
min_shares = min(s['shares'] for s in portfolio)
print(f"Minimum shares in any holding: {min_shares}")

# Verifique se alguma ação é IBM
has_ibm = any(s['name'] == 'IBM' for s in portfolio)
print(f"Portfolio contains IBM: {has_ibm}")

# Verifique se todas as ações são IBM
all_ibm = all(s['name'] == 'IBM' for s in portfolio)
print(f"All stocks are IBM: {all_ibm}")

# Conte as ações da IBM
ibm_shares = sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
print(f"Total IBM shares: {ibm_shares}")
```

As expressões geradoras também são úteis para operações de string. Veja como unir valores em uma tupla:

```python
s = ('GOOG', 100, 490.10)
# Isso falharia: ','.join(s)
# Use uma expressão geradora para converter todos os itens em strings
joined = ','.join(str(x) for x in s)
print(joined)  # Saída: 'GOOG,100,490.1'
```

A principal vantagem de usar expressões geradoras nesses exemplos é que nenhuma lista intermediária é criada, resultando em um código mais eficiente em termos de memória.
