# Compreendendo os Geradores Python

Geradores são um recurso poderoso em Python. Eles oferecem uma maneira simples e elegante de criar iteradores. Em Python, quando você lida com sequências de dados, os iteradores são muito úteis, pois permitem que você percorra uma série de valores um por um. Funções regulares normalmente retornam um único valor e, em seguida, param de executar. No entanto, os geradores são diferentes. Eles podem produzir uma sequência de valores ao longo do tempo, o que significa que podem produzir múltiplos valores de forma gradual.

## O que é um Gerador?

Uma função geradora tem uma aparência semelhante a uma função regular. Mas a diferença fundamental reside em como ela retorna valores. Em vez de usar a instrução `return` para fornecer um único resultado, uma função geradora usa a instrução `yield`. A instrução `yield` é especial. Cada vez que é executada, o estado da função é pausado, e o valor que segue a palavra-chave `yield` é retornado ao chamador. Quando a função geradora é chamada novamente, ela retoma a execução exatamente de onde parou.

Vamos começar criando uma função geradora simples. A função `range()` embutida em Python não suporta passos fracionários. Então, criaremos uma função geradora que pode produzir uma faixa de números com um passo fracionário.

1. Primeiro, você precisa abrir um novo terminal Python no WebIDE. Para fazer isso, clique no menu "Terminal" e selecione "Novo Terminal".
2. Depois que o terminal estiver aberto, digite o seguinte código no terminal. Este código define uma função geradora e, em seguida, a testa.

```python
def frange(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

# Test the generator with a for loop
for x in frange(0, 2, 0.25):
    print(x, end=' ')
```

Neste código, a função `frange` é uma função geradora. Ela inicializa uma variável `current` com o valor `start`. Então, enquanto `current` for menor que o valor `stop`, ela produz o valor `current` e, em seguida, incrementa `current` pelo valor `step`. O loop `for` então itera sobre os valores produzidos pela função geradora `frange` e os imprime.

Você deve ver a seguinte saída:

```
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

## A Natureza Única dos Geradores

Uma característica importante dos geradores é que eles são exauríveis. Isso significa que, uma vez que você iterou por todos os valores produzidos por um gerador, ele não pode ser usado novamente para produzir a mesma sequência de valores. Vamos demonstrar isso com o seguinte código:

```python
# Create a generator object
f = frange(0, 2, 0.25)

# First iteration works fine
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

# Second iteration produces nothing
print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

Neste código, primeiro criamos um objeto gerador `f` usando a função `frange`. O primeiro loop `for` itera sobre todos os valores produzidos pelo gerador e os imprime. Após a primeira iteração, o gerador foi exaurido, o que significa que ele já produziu todos os valores que pode. Então, quando tentamos iterar sobre ele novamente no segundo loop `for`, ele não produz nenhum valor novo.

Saída:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:

```

Observe que a segunda iteração não produziu nenhuma saída porque o gerador já estava exaurido.

## Criando Geradores Reutilizáveis com Classes

Se você precisar iterar várias vezes sobre a mesma sequência de valores, pode encapsular o gerador em uma classe. Ao fazer isso, cada vez que você iniciar uma nova iteração, um novo gerador será criado.

```python
class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        n = self.start
        while n < self.stop:
            yield n
            n += self.step

# Create an instance
f = FRange(0, 2, 0.25)

# We can iterate multiple times
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

Neste código, definimos uma classe `FRange`. O método `__init__` inicializa os valores `start`, `stop` e `step`. O método `__iter__` é um método especial em classes Python. Ele é usado para criar um iterador. Dentro do método `__iter__`, temos um gerador que produz valores de maneira semelhante à função `frange` que definimos anteriormente.

Quando criamos uma instância `f` da classe `FRange` e iteramos sobre ela várias vezes, cada iteração chama o método `__iter__`, que cria um novo gerador. Então, podemos obter a mesma sequência de valores várias vezes.

Saída:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

Desta vez, podemos iterar várias vezes porque o método `__iter__()` cria um novo gerador cada vez que é chamado.
