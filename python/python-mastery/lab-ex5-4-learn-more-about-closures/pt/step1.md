# _Closures_ como uma Estrutura de Dados

Em Python, _closures_ oferecem uma maneira poderosa de encapsular dados. Encapsulamento significa manter os dados privados e controlar o acesso a eles. Com _closures_, você pode criar funções que gerenciam e modificam dados privados sem ter que usar classes ou variáveis globais. Variáveis globais podem ser acessadas e modificadas de qualquer lugar no seu código, o que pode levar a comportamentos inesperados. Classes, por outro lado, exigem uma estrutura mais complexa. _Closures_ fornecem uma alternativa mais simples para encapsulamento de dados.

Vamos criar um arquivo chamado `counter.py` para demonstrar este conceito:

1. Abra o WebIDE e crie um novo arquivo chamado `counter.py` no diretório `/home/labex/project`. É aqui que escreveremos o código que define nosso contador baseado em _closure_.

2. Adicione o seguinte código ao arquivo:

```python
def counter(value):
    """
    Cria um contador com funções de incremento e decremento.

    Args:
        value: Valor inicial do contador

    Returns:
        Duas funções: uma para incrementar o contador, outra para decrementá-lo
    """
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

Neste código, definimos uma função chamada `counter()`. Esta função recebe um `value` inicial como argumento. Dentro da função `counter()`, definimos duas funções internas: `incr()` e `decr()`. Essas funções internas compartilham o acesso à mesma variável `value`. A palavra-chave `nonlocal` é usada para dizer ao Python que queremos modificar a variável `value` do escopo envolvente (a função `counter()`). Sem a palavra-chave `nonlocal`, o Python criaria uma nova variável local dentro das funções internas em vez de modificar o `value` do escopo externo.

3. Agora, vamos criar um arquivo de teste para ver isso em ação. Crie um novo arquivo chamado `test_counter.py` com o seguinte conteúdo:

```python
from counter import counter

# Cria um contador começando em 0
up, down = counter(0)

# Incrementa o contador várias vezes
print("Incrementando o contador:")
print(up())  # Deve imprimir 1
print(up())  # Deve imprimir 2
print(up())  # Deve imprimir 3

# Decrementa o contador
print("\nDecrementando o contador:")
print(down())  # Deve imprimir 2
print(down())  # Deve imprimir 1
```

Neste arquivo de teste, primeiro importamos a função `counter()` do arquivo `counter.py`. Em seguida, criamos um contador começando em 0 chamando `counter(0)` e desempacotando as funções retornadas em `up` e `down`. Em seguida, chamamos a função `up()` várias vezes para incrementar o contador e imprimir os resultados. Depois disso, chamamos a função `down()` para decrementar o contador e imprimir os resultados.

4. Execute o arquivo de teste executando o seguinte comando no terminal:

```bash
python3 test_counter.py
```

Você deve ver a seguinte saída:

```
Incrementando o contador:
1
2
3

Decrementando o contador:
2
1
```

Observe como não há nenhuma definição de classe envolvida aqui. As funções `up()` e `down()` estão manipulando um valor compartilhado que não é nem uma variável global nem um atributo de instância. Este valor é armazenado no _closure_, tornando-o acessível apenas às funções retornadas por `counter()`.

Este é um exemplo de como _closures_ podem ser usados como uma estrutura de dados. A variável encapsulada `value` é mantida entre as chamadas de função, e é privada para as funções que a acessam. Isso significa que nenhuma outra parte do seu código pode acessar ou modificar diretamente esta variável `value`, fornecendo um nível de proteção de dados.
