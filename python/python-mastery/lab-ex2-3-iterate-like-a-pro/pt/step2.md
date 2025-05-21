# Usando as Funções `enumerate()` e `zip()`

Nesta etapa, vamos explorar duas funções embutidas incrivelmente úteis em Python que são essenciais para a iteração: `enumerate()` e `zip()`. Essas funções podem simplificar significativamente seu código quando você estiver trabalhando com sequências.

## Contando com `enumerate()`

Ao iterar sobre uma sequência, você pode frequentemente precisar acompanhar o índice ou a posição de cada item. É aí que a função `enumerate()` é útil. A função `enumerate()` recebe uma sequência como entrada e retorna pares de (índice, valor) para cada item nessa sequência.

Se você esteve acompanhando no interpretador Python da etapa anterior, pode continuar usando-o. Caso contrário, inicie uma nova sessão. Veja como você pode configurar os dados se estiver começando do zero:

```python
# Se você estiver iniciando uma nova sessão, recarregue os dados primeiro:
# import csv
# f = open('portfolio.csv')
# f_csv = csv.reader(f)
# headers = next(f_csv)
# rows = list(f_csv)

# Use enumerate para obter os números das linhas
for rowno, row in enumerate(rows):
    print(rowno, row)
```

Quando você executa o código acima, a função `enumerate(rows)` gerará pares de um índice (começando em 0) e a linha correspondente da sequência `rows`. O loop `for` então desempacota esses pares nas variáveis `rowno` e `row`, e nós os imprimimos.

Saída:

```
0 ['AA', '100', '32.20']
1 ['IBM', '50', '91.10']
2 ['CAT', '150', '83.44']
3 ['MSFT', '200', '51.23']
4 ['GE', '95', '40.37']
5 ['MSFT', '50', '65.10']
6 ['IBM', '100', '70.44']
```

Podemos tornar o código ainda mais legível combinando `enumerate()` com desempacotamento. O desempacotamento nos permite atribuir diretamente os elementos de uma sequência a variáveis individuais.

```python
for rowno, (name, shares, price) in enumerate(rows):
    print(rowno, name, shares, price)
```

Neste código, estamos usando um par extra de parênteses em torno de `(name, shares, price)` para desempacotar corretamente os dados da linha. O `enumerate(rows)` ainda nos dá o índice e a linha, mas agora estamos desempacotando a linha nas variáveis `name`, `shares` e `price`.

Saída:

```
0 AA 100 32.20
1 IBM 50 91.10
2 CAT 150 83.44
3 MSFT 200 51.23
4 GE 95 40.37
5 MSFT 50 65.10
6 IBM 100 70.44
```

## Emparelhando Dados com `zip()`

A função `zip()` é outra ferramenta poderosa em Python. Ela é usada para combinar elementos correspondentes de múltiplas sequências. Quando você passa múltiplas sequências para `zip()`, ela cria um iterador que produz tuplas, onde cada tupla contém elementos de cada uma das sequências de entrada na mesma posição.

Vamos ver como podemos usar `zip()` com os dados `headers` e `row` com os quais temos trabalhado.

```python
# Lembre-se da variável headers de antes
print(headers)  # Deve mostrar ['name', 'shares', 'price']

# Obtenha a primeira linha
row = rows[0]
print(row)      # Deve mostrar ['AA', '100', '32.20']

# Use zip para emparelhar nomes de colunas com valores
for col, val in zip(headers, row):
    print(col, val)
```

Neste código, `zip(headers, row)` pega a sequência `headers` e a sequência `row` e emparelha seus elementos correspondentes. O loop `for` então desempacota esses pares em `col` (para o nome da coluna de `headers`) e `val` (para o valor de `row`), e nós os imprimimos.

Saída:

```
['name', 'shares', 'price']
['AA', '100', '32.20']
name AA
shares 100
price 32.20
```

Um uso muito comum de `zip()` é criar dicionários a partir de pares chave-valor. Em Python, um dicionário é uma coleção de pares chave-valor.

```python
# Crie um dicionário a partir de cabeçalhos e valores de linha
record = dict(zip(headers, row))
print(record)
```

Aqui, `zip(headers, row)` cria pares de nomes de colunas e valores, e a função `dict()` pega esses pares e os transforma em um dicionário.

Saída:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
```

Podemos estender essa ideia para converter todas as linhas em nossa sequência `rows` em dicionários.

```python
# Converta todas as linhas em dicionários
for row in rows:
    record = dict(zip(headers, row))
    print(record)
```

Neste loop, para cada linha em `rows`, usamos `zip(headers, row)` para criar pares chave-valor e, em seguida, `dict()` para transformar esses pares em um dicionário. Essa técnica é muito comum em aplicações de processamento de dados, especialmente ao trabalhar com arquivos CSV, onde a primeira linha contém cabeçalhos.

Saída:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'IBM', 'shares': '50', 'price': '91.10'}
{'name': 'CAT', 'shares': '150', 'price': '83.44'}
{'name': 'MSFT', 'shares': '200', 'price': '51.23'}
{'name': 'GE', 'shares': '95', 'price': '40.37'}
{'name': 'MSFT', 'shares': '50', 'price': '65.10'}
{'name': 'IBM', 'shares': '100', 'price': '70.44'}
```
