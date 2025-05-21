# Compreendendo a instrução `yield from`

Nesta etapa, vamos explorar a instrução `yield from` em Python. Esta instrução é uma ferramenta poderosa ao trabalhar com geradores, e simplifica o processo de delegação de operações a outros geradores. Ao final desta etapa, você entenderá o que é `yield from`, como funciona e como pode lidar com a passagem de valores entre diferentes geradores.

## O que é `yield from`?

A instrução `yield from` foi introduzida no Python 3.3. Seu principal objetivo é simplificar a delegação de operações a subgeradores. Um subgerador é apenas outro gerador ao qual um gerador principal pode delegar trabalho.

Normalmente, quando você deseja que um gerador produza valores de outro gerador, você precisaria usar um loop. Por exemplo, sem `yield from`, você escreveria um código como este:

```python
def delegating_generator():
    for value in subgenerator():
        yield value
```

Neste código, o `delegating_generator` usa um loop `for` para iterar sobre os valores produzidos por `subgenerator` e, em seguida, produz cada valor um por um.

No entanto, com a instrução `yield from`, o código se torna muito mais simples:

```python
def delegating_generator():
    yield from subgenerator()
```

Esta única linha de código atinge o mesmo resultado que o loop no exemplo anterior. Mas `yield from` não é apenas um atalho. Ele também gerencia a comunicação bidirecional entre o chamador e o subgerador. Isso significa que quaisquer valores enviados ao gerador delegador são passados diretamente para o subgerador.

## Exemplo Básico

Vamos criar um exemplo simples para ver como `yield from` funciona na prática.

1. Primeiro, precisamos abrir o arquivo `cofollow.py` no editor. Para fazer isso, usaremos o comando `cd` para navegar até o diretório correto. Execute o seguinte comando no terminal:

```bash
cd /home/labex/project
```

2. Em seguida, adicionaremos duas funções ao arquivo `cofollow.py`. A função `subgen` é um gerador simples que produz os números de 0 a 4. A função `main_gen` usa `yield from` para delegar a geração desses números a `subgen` e, em seguida, produz a string `'Done'`. Adicione o seguinte código ao final do arquivo `cofollow.py`:

```python
def subgen():
    for i in range(5):
        yield i

def main_gen():
    yield from subgen()
    yield 'Done'
```

3. Agora, vamos testar essas funções. Abra um shell Python e execute o seguinte código:

```python
from cofollow import subgen, main_gen

# Test subgen directly
for x in subgen():
    print(x)

# Test main_gen that delegates to subgen
for x in main_gen():
    print(x)
```

Quando você executar este código, deverá ver a seguinte saída:

```
0
1
2
3
4

0
1
2
3
4
Done
```

Esta saída mostra que `yield from` permite que `main_gen` passe todos os valores gerados por `subgen` diretamente para o chamador.

## Passagem de Valores com `yield from`

Uma das características mais poderosas de `yield from` é sua capacidade de lidar com a passagem de valores em ambas as direções. Vamos criar um exemplo mais complexo para demonstrar isso.

1. Adicione as seguintes funções ao arquivo `cofollow.py`:

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

def caller():
    acc = accumulator()
    yield from acc
    yield 'Total accumulated'
```

A função `accumulator` é uma corrotina que acompanha um total acumulado. Ela produz o total atual e, em seguida, espera receber um novo valor. Se receber `None`, interrompe o loop. A função `caller` cria uma instância de `accumulator` e usa `yield from` para delegar todas as operações de envio e recebimento a ela.

2. Teste essas funções em um shell Python:

```python
from cofollow import caller

c = caller()
print(next(c))  # Start the coroutine
print(c.send(1))  # Send value 1, get accumulated value
print(c.send(2))  # Send value 2, get accumulated value
print(c.send(3))  # Send value 3, get accumulated value
print(c.send(None))  # Send None to exit the accumulator
```

Quando você executar este código, deverá ver a seguinte saída:

```
0
1
3
6
'Total accumulated'
```

Esta saída mostra que `yield from` delega totalmente todas as operações de envio e recebimento ao subgerador até que ele seja esgotado.

Agora que você entende o básico de `yield from`, passaremos para aplicações mais práticas na próxima etapa.
