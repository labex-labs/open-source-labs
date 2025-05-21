# Compreendendo a Passagem de Argumentos de Funções

Em Python, as funções são um conceito fundamental que permite agrupar um conjunto de instruções para realizar uma tarefa específica. Ao chamar uma função, você frequentemente precisa fornecer alguns dados, que chamamos de argumentos. Python oferece diferentes maneiras de passar esses argumentos para as funções. Essa flexibilidade é incrivelmente útil, pois ajuda a escrever um código mais limpo e fácil de manter. Antes de começarmos a aplicar essas técnicas ao nosso projeto, vamos dar uma olhada mais de perto nessas convenções de passagem de argumentos.

## Criando um Backup do Seu Trabalho

Antes de começarmos a fazer alterações no nosso arquivo `stock.py`, é uma boa prática criar um backup. Dessa forma, se algo der errado durante nossa experimentação, sempre podemos voltar à versão original. Para criar um backup, abra um terminal e execute o seguinte comando:

```bash
cp stock.py orig_stock.py
```

Este comando usa o comando `cp` (copy) no terminal. Ele pega o arquivo `stock.py` e cria uma cópia dele chamada `orig_stock.py`. Ao fazer isso, garantimos que nosso trabalho original seja preservado com segurança.

## Explorando a Passagem de Argumentos de Funções

Em Python, existem várias maneiras de chamar funções com diferentes tipos de argumentos. Vamos explorar cada um desses métodos em detalhes.

### 1. Argumentos Posicionais

A maneira mais simples de passar argumentos para uma função é por posição. Ao definir uma função, você especifica uma lista de parâmetros. Ao chamar a função, você fornece valores para esses parâmetros na mesma ordem em que são definidos.

Aqui está um exemplo:

```python
def calculate(x, y, z):
    return x + y + z

# Chamada com argumentos posicionais
result = calculate(1, 2, 3)
print(result)  # Output: 6
```

Neste exemplo, a função `calculate` recebe três parâmetros: `x`, `y` e `z`. Quando chamamos a função com `calculate(1, 2, 3)`, o valor `1` é atribuído a `x`, `2` é atribuído a `y` e `3` é atribuído a `z`. A função então soma esses valores e retorna o resultado.

### 2. Argumentos de Palavra-chave (Keyword Arguments)

Além dos argumentos posicionais, você também pode especificar argumentos por seus nomes. Isso é chamado de uso de argumentos de palavra-chave. Quando você usa argumentos de palavra-chave, não precisa se preocupar com a ordem dos argumentos.

Aqui está um exemplo:

```python
# Chamada com uma mistura de argumentos posicionais e de palavra-chave
result = calculate(1, z=3, y=2)
print(result)  # Output: 6
```

Neste exemplo, primeiro passamos o argumento posicional `1` para `x`. Em seguida, usamos argumentos de palavra-chave para especificar os valores para `y` e `z`. A ordem dos argumentos de palavra-chave não importa, desde que você forneça os nomes corretos.

### 3. Desempacotando Sequências e Dicionários

Python fornece uma maneira conveniente de passar sequências e dicionários como argumentos usando a sintaxe `*` e `**`. Isso é chamado de desempacotamento (unpacking).

Aqui está um exemplo de desempacotamento de uma tupla em argumentos posicionais:

```python
# Desempacotando uma tupla em argumentos posicionais
args = (1, 2, 3)
result = calculate(*args)
print(result)  # Output: 6
```

Neste exemplo, temos uma tupla `args` que contém os valores `1`, `2` e `3`. Quando usamos o operador `*` antes de `args` na chamada da função, Python desempacota a tupla e passa seus elementos como argumentos posicionais para a função `calculate`.

Aqui está um exemplo de desempacotamento de um dicionário em argumentos de palavra-chave:

```python
# Desempacotando um dicionário em argumentos de palavra-chave
kwargs = {'y': 2, 'z': 3}
result = calculate(1, **kwargs)
print(result)  # Output: 6
```

Neste exemplo, temos um dicionário `kwargs` que contém os pares chave-valor `'y': 2` e `'z': 3`. Quando usamos o operador `**` antes de `kwargs` na chamada da função, Python desempacota o dicionário e passa seus pares chave-valor como argumentos de palavra-chave para a função `calculate`.

### 4. Aceitando Argumentos Variáveis

Às vezes, você pode querer definir uma função que pode aceitar qualquer número de argumentos. Python permite que você faça isso usando a sintaxe `*` e `**` na definição da função.

Aqui está um exemplo de uma função que aceita qualquer número de argumentos posicionais:

```python
# Aceitar qualquer número de argumentos posicionais
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2))           # Output: 3
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
```

Neste exemplo, a função `sum_all` usa o parâmetro `*args` para aceitar qualquer número de argumentos posicionais. O operador `*` coleta todos os argumentos posicionais em uma tupla chamada `args`. A função então usa a função `sum` embutida para somar todos os elementos na tupla.

Aqui está um exemplo de uma função que aceita qualquer número de argumentos de palavra-chave:

```python
# Aceitar qualquer número de argumentos de palavra-chave
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Python", year=1991)
# Output:
# name: Python
# year: 1991
```

Neste exemplo, a função `print_info` usa o parâmetro `**kwargs` para aceitar qualquer número de argumentos de palavra-chave. O operador `**` coleta todos os argumentos de palavra-chave em um dicionário chamado `kwargs`. A função então itera sobre os pares chave-valor no dicionário e os imprime.

Essas técnicas nos ajudarão a criar estruturas de código mais flexíveis e reutilizáveis nos próximos passos. Para se sentir mais confortável com esses conceitos, vamos abrir o interpretador Python e experimentar alguns desses exemplos.

```bash
python3
```

Depois de estar no interpretador Python, tente inserir os exemplos acima. Isso lhe dará experiência prática com essas técnicas de passagem de argumentos.
