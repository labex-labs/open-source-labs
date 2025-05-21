# Usando `yield from` em Corrotinas

Nesta etapa, exploraremos como usar a instrução `yield from` com corrotinas para aplicações mais práticas. Corrotinas são um conceito poderoso em Python, e entender como usar `yield from` com elas pode simplificar muito seu código.

## Corrotinas e Passagem de Mensagens

Corrotinas são funções especiais que podem receber valores através da instrução `yield`. Elas são incrivelmente úteis para tarefas como processamento de dados e tratamento de eventos. No arquivo `cofollow.py`, existe um decorador `consumer`. Este decorador ajuda a configurar corrotinas, avançando-as automaticamente para o primeiro ponto `yield`. Isso significa que você não precisa iniciar a corrotina manualmente; o decorador cuida disso para você.

Vamos criar uma corrotina que recebe valores e valida seus tipos. Veja como você pode fazer isso:

1. Primeiro, abra o arquivo `cofollow.py` no editor. Você pode usar o seguinte comando no terminal para navegar até o diretório correto:

```bash
cd /home/labex/project
```

2. Em seguida, adicione a seguinte função `receive` ao final do arquivo `cofollow.py`. Esta função é uma corrotina que receberá uma mensagem e validará seu tipo.

```python
def receive(expected_type):
    """
    A corrotina que recebe uma mensagem e valida seu tipo.
    Retorna a mensagem recebida se corresponder ao tipo esperado.
    """
    msg = yield
    assert isinstance(msg, expected_type), f'Expected type {expected_type}'
    return msg
```

Aqui está o que esta função faz:

- Ela usa `yield` sem uma expressão para receber um valor. Quando a corrotina recebe um valor, esta instrução `yield` o capturará.
- Ela verifica se o valor recebido é do tipo esperado usando a função `isinstance`. Se o tipo não corresponder, ela levanta um `AssertionError`.
- Se a verificação de tipo passar, ela retorna o valor.

3. Agora, vamos criar uma corrotina que usa `yield from` com nossa função `receive`. Esta nova corrotina receberá e imprimirá apenas inteiros.

```python
@consumer
def print_ints():
    """
    A corrotina que recebe e imprime apenas inteiros.
    Usa yield from para delegar à corrotina receive.
    """
    while True:
        val = yield from receive(int)
        print('Got:', val)
```

4. Para testar esta corrotina, abra um shell Python e execute o seguinte código:

```python
from cofollow import print_ints

p = print_ints()
p.send(42)
p.send(13)
try:
    p.send('13')  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

Você deve ver a seguinte saída:

```
Got: 42
Got: 13
Error: Expected type <class 'int'>
```

## Compreendendo como `yield from` funciona com Corrotinas

Quando usamos `yield from receive(int)` na corrotina `print_ints`, as seguintes etapas ocorrem:

1. O controle é delegado à corrotina `receive`. Isso significa que a corrotina `print_ints` pausa, e a corrotina `receive` começa a executar.
2. A corrotina `receive` usa `yield` para receber um valor. Ela espera que um valor seja enviado a ela.
3. Quando um valor é enviado para `print_ints`, ele é realmente recebido por `receive`. A instrução `yield from` cuida de passar o valor de `print_ints` para `receive`.
4. A corrotina `receive` valida o tipo do valor recebido. Se o tipo estiver correto, ela retorna o valor.
5. O valor retornado se torna o resultado da expressão `yield from` na corrotina `print_ints`. Isso significa que a variável `val` em `print_ints` recebe o valor retornado por `receive`.

Usar `yield from` torna o código mais legível do que se tivéssemos que lidar com a produção e recebimento diretamente. Ele abstrai a complexidade da passagem de valores entre corrotinas.

## Criando Corrotinas de Verificação de Tipo Mais Avançadas

Vamos expandir nossas funções utilitárias para lidar com uma validação de tipo mais complexa. Veja como você pode fazer isso:

1. Adicione as seguintes funções ao arquivo `cofollow.py`:

```python
def receive_dict():
    """Receive and validate a dictionary"""
    result = yield from receive(dict)
    return result

def receive_str():
    """Receive and validate a string"""
    result = yield from receive(str)
    return result

@consumer
def process_data():
    """Process different types of data using the receive utilities"""
    while True:
        print("Waiting for a string...")
        name = yield from receive_str()
        print(f"Got string: {name}")

        print("Waiting for a dictionary...")
        data = yield from receive_dict()
        print(f"Got dictionary with {len(data)} items: {data}")

        print("Processing complete for this round.")
```

2. Para testar a nova corrotina, abra um shell Python e execute o seguinte código:

```python
from cofollow import process_data

proc = process_data()
proc.send("John Doe")
proc.send({"age": 30, "city": "New York"})
proc.send("Jane Smith")
try:
    proc.send(123)  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

Você deve ver uma saída como esta:

```
Waiting for a string...
Got string: John Doe
Waiting for a dictionary...
Got dictionary with 2 items: {'age': 30, 'city': 'New York'}
Processing complete for this round.
Waiting for a string...
Got string: Jane Smith
Waiting for a dictionary...
Error: Expected type <class 'dict'>
```

A instrução `yield from` torna o código mais limpo e legível. Ela nos permite focar na lógica de alto nível do nosso programa, em vez de ficarmos atolados nos detalhes da passagem de mensagens entre corrotinas.
