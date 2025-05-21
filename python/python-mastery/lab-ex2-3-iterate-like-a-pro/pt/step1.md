# Iteração Básica e Desempacotamento de Sequências

Nesta etapa, exploraremos a iteração básica usando loops `for` e o desempacotamento de sequências em Python. A iteração é um conceito fundamental na programação, permitindo que você percorra cada item em uma sequência, um por um. O desempacotamento de sequências, por outro lado, permite que você atribua elementos individuais de uma sequência a variáveis de forma conveniente.

## Carregando Dados de um Arquivo CSV

Vamos começar carregando alguns dados de um arquivo CSV. CSV (Valores Separados por Vírgula) é um formato de arquivo comum usado para armazenar dados tabulares. Para começar, precisamos abrir um terminal no WebIDE e iniciar o interpretador Python. Isso nos permitirá executar o código Python interativamente.

```bash
cd ~/project
python3
```

Agora que estamos no interpretador Python, podemos executar o seguinte código Python para ler dados do arquivo `portfolio.csv`. Primeiro, importamos o módulo `csv`, que fornece funcionalidade para trabalhar com arquivos CSV. Em seguida, abrimos o arquivo e criamos um objeto `csv.reader` para ler os dados. Usamos a função `next` para obter os cabeçalhos das colunas e convertemos os dados restantes em uma lista. Finalmente, usamos a função `pprint` do módulo `pprint` para imprimir as linhas em um formato mais legível.

```python
import csv

f = open('portfolio.csv')
f_csv = csv.reader(f)
headers = next(f_csv)    # Get the column headers
rows = list(f_csv)       # Convert the remaining data to a list
from pprint import pprint
pprint(rows)             # Pretty print the rows
```

Você deve ver uma saída semelhante a esta:

```
[['AA', '100', '32.20'],
 ['IBM', '50', '91.10'],
 ['CAT', '150', '83.44'],
 ['MSFT', '200', '51.23'],
 ['GE', '95', '40.37'],
 ['MSFT', '50', '65.10'],
 ['IBM', '100', '70.44']]
```

## Iteração Básica com Loops `for`

A instrução `for` em Python é usada para iterar sobre qualquer sequência de dados, como uma lista, tupla ou string. Em nosso caso, usaremos para iterar sobre as linhas de dados que carregamos do arquivo CSV.

```python
for row in rows:
    print(row)
```

Este código percorrerá cada linha na lista `rows` e a imprimirá. Você verá cada linha de dados do nosso arquivo CSV impressa uma por uma.

```
['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
```

## Desempacotamento de Sequências em Loops

Python permite que você desempacote sequências diretamente em um loop `for`. Isso é muito útil quando você conhece a estrutura de cada item na sequência. Em nosso caso, cada linha na lista `rows` contém três elementos: um nome, o número de ações e o preço. Podemos desempacotar esses elementos diretamente no loop `for`.

```python
for name, shares, price in rows:
    print(name, shares, price)
```

Este código desempacotará cada linha nas variáveis `name`, `shares` e `price` e, em seguida, as imprimirá. Você verá os dados impressos em um formato mais legível.

```
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
```

Se você não precisar de alguns valores, pode usar `_` como um espaço reservado para indicar que você não se importa com esses valores. Por exemplo, se você quiser imprimir apenas o nome e o preço, pode usar o seguinte código:

```python
for name, _, price in rows:
    print(name, price)
```

Este código ignorará o segundo elemento em cada linha e imprimirá apenas o nome e o preço.

```
AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
```

## Desempacotamento Estendido com o Operador `*`

Para um desempacotamento mais avançado, você pode usar o operador `*` como um curinga. Isso permite que você colete vários elementos em uma lista. Vamos agrupar nossos dados por nome usando esta técnica.

```python
from collections import defaultdict

byname = defaultdict(list)
for name, *data in rows:
    byname[name].append(data)

# Print the data for IBM
print(byname['IBM'])

# Iterate through IBM's data
for shares, price in byname['IBM']:
    print(shares, price)
```

Neste código, primeiro importamos a classe `defaultdict` do módulo `collections`. Um `defaultdict` é um dicionário que cria automaticamente um novo valor (neste caso, uma lista vazia) se a chave não existir. Em seguida, usamos o operador `*` para coletar todos os elementos, exceto o primeiro, em uma lista chamada `data`. Armazenamos esta lista no dicionário `byname`, agrupada por nome. Finalmente, imprimimos os dados para IBM e iteramos sobre eles para imprimir as ações e o preço.

Saída:

```
[['50', '91.10'], ['100', '70.44']]
50 91.10
100 70.44
```

Neste exemplo, `*data` coleta todos os itens, exceto o primeiro, em uma lista, que então armazenamos em um dicionário agrupado por nome. Esta é uma técnica poderosa para lidar com dados com sequências de comprimento variável.
