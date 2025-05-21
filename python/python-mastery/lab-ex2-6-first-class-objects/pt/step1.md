# Compreendendo Objetos de Primeira Classe em Python

Em Python, tudo é tratado como um objeto. Isso inclui funções e tipos. O que isso significa? Bem, significa que você pode armazenar funções e tipos em estruturas de dados, passá-los como argumentos para outras funções e até mesmo retorná-los de outras funções. Este é um conceito muito poderoso, e vamos explorá-lo usando o processamento de dados CSV como exemplo.

## Explorando Tipos de Primeira Classe

Primeiro, vamos iniciar o interpretador Python. Abra um novo terminal no WebIDE e digite o seguinte comando. Este comando iniciará o interpretador Python, que é onde executaremos nosso código Python.

```bash
python3
```

Ao trabalhar com arquivos CSV em Python, frequentemente precisamos converter as strings que lemos desses arquivos em tipos de dados apropriados. Por exemplo, um número em um arquivo CSV pode ser lido como uma string, mas queremos usá-lo como um inteiro ou um float em nosso código Python. Para fazer isso, podemos criar uma lista de funções de conversão.

```python
coltypes = [str, int, float]
```

Observe que estamos criando uma lista que contém as funções de tipo reais, não strings. Em Python, os tipos são objetos de primeira classe, o que significa que podemos tratá-los como qualquer outro objeto. Podemos colocá-los em listas, passá-los e usá-los em nosso código.

Agora, vamos ler alguns dados de um arquivo CSV de portfólio para ver como podemos usar essas funções de conversão.

```python
import csv
f = open('portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(row)
```

Quando você executar este código, deverá ver uma saída semelhante à seguinte. Esta é a primeira linha de dados do arquivo CSV, representada como uma lista de strings.

```
['AA', '100', '32.20']
```

Em seguida, usaremos a função `zip`. A função `zip` recebe múltiplos iteráveis (como listas ou tuplas) e emparelha seus elementos. Usaremos para emparelhar cada valor da linha com sua função de conversão de tipo correspondente.

```python
r = list(zip(coltypes, row))
print(r)
```

Isso produzirá a seguinte saída. Cada par contém uma função de tipo e um valor de string do arquivo CSV.

```
[(<class 'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>, '32.20')]
```

Agora que temos esses pares, podemos aplicar cada função para converter os valores em seus tipos apropriados.

```python
record = [func(val) for func, val in zip(coltypes, row)]
print(record)
```

A saída mostrará que os valores foram convertidos para seus tipos apropriados. A string 'AA' permanece uma string, '100' se torna o inteiro 100, e '32.20' se torna o float 32.2.

```
['AA', 100, 32.2]
```

Também podemos combinar esses valores com seus nomes de coluna para criar um dicionário. Um dicionário é uma estrutura de dados útil em Python que nos permite armazenar pares chave-valor.

```python
record_dict = dict(zip(headers, record))
print(record_dict)
```

A saída será um dicionário onde as chaves são os nomes das colunas e os valores são os dados convertidos.

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Você pode executar todas essas etapas em uma única compreensão. Uma compreensão é uma maneira concisa de criar listas, dicionários ou conjuntos em Python.

```python
result = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
print(result)
```

A saída será o mesmo dicionário de antes.

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Quando terminar de trabalhar no interpretador Python, você pode sair digitando o seguinte comando.

```python
exit()
```

Esta demonstração mostra como o tratamento de funções do Python como objetos de primeira classe permite técnicas poderosas de processamento de dados. Ao poder tratar tipos e funções como objetos, podemos escrever um código mais flexível e conciso.
