# Criação Manual de Classes

Na programação Python, as classes são um conceito fundamental que permite agrupar dados e funções. Normalmente, definimos classes usando a sintaxe padrão do Python. Por exemplo, aqui está uma classe `Stock` simples. Esta classe representa uma ação com atributos como `name` (nome), `shares` (ações) e `price` (preço), e possui métodos para calcular o custo e vender ações.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Mas você já se perguntou como o Python realmente cria uma classe nos bastidores? E se quiséssemos criar esta classe sem usar a sintaxe padrão de classe? Nesta seção, exploraremos como as classes Python são construídas em um nível inferior.

## Iniciar o Shell Interativo do Python

Para começar a experimentar a criação manual de classes, precisamos abrir um shell interativo do Python. Este shell nos permite executar o código Python linha por linha, o que é ótimo para aprender e testar.

Abra um terminal no WebIDE e inicie o shell interativo do Python digitando os seguintes comandos. O primeiro comando `cd ~/project` altera o diretório atual para o diretório do projeto, e o segundo comando `python3` inicia o shell interativo do Python 3.

```bash
cd ~/project
python3
```

## Definindo Métodos como Funções Regulares

Antes de criarmos uma classe manualmente, precisamos definir os métodos que farão parte da classe. Em Python, os métodos são apenas funções que estão associadas a uma classe. Então, vamos definir os métodos que queremos em nossa classe como funções Python regulares.

```python
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

def sell(self, nshares):
    self.shares -= nshares
```

Aqui, a função `__init__` é um método especial nas classes Python. É chamado de construtor e é usado para inicializar os atributos do objeto quando uma instância da classe é criada. O método `cost` calcula o custo total das ações, e o método `sell` reduz o número de ações.

## Criando um Dicionário de Métodos

Agora que definimos nossos métodos como funções regulares, precisamos organizá-los de uma forma que o Python possa entender ao criar a classe. Fazemos isso criando um dicionário que conterá todos os métodos para nossa classe.

```python
methods = {
    '__init__': __init__,
    'cost': cost,
    'sell': sell
}
```

Neste dicionário, as chaves são os nomes dos métodos como serão usados na classe, e os valores são os objetos de função reais que definimos anteriormente.

## Usando o Construtor `type()` para Criar uma Classe

Em Python, a função `type()` é uma função embutida que pode ser usada para criar classes em um nível inferior. A função `type()` recebe três argumentos:

1.  O nome da classe: Esta é uma string que representa o nome da classe que queremos criar.
2.  Uma tupla de classes base: Em Python, as classes podem herdar de outras classes. Aqui, usamos `(object,)` o que significa que nossa classe herda da classe base `object`, que é a classe base para todas as classes em Python.
3.  Um dicionário contendo métodos e atributos: Este é o dicionário que criamos anteriormente que contém todos os métodos da nossa classe.

```python
Stock = type('Stock', (object,), methods)
```

Esta linha de código cria uma nova classe chamada `Stock` usando a função `type()`. A classe herda da classe `object` e possui os métodos definidos no dicionário `methods`.

## Testando Nossa Classe Criada Manualmente

Agora que criamos nossa classe manualmente, vamos testá-la para garantir que ela funcione como esperado. Criaremos uma instância de nossa nova classe e chamaremos seus métodos.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
s.sell(25)
print(s.shares)
```

Na primeira linha, criamos uma instância da classe `Stock` com o nome `GOOG`, 100 ações e um preço de 490.10. Em seguida, imprimimos o nome da ação, calculamos e imprimimos o custo, vendemos 25 ações e, finalmente, imprimimos o número restante de ações.

Você deve ver a seguinte saída:

```
GOOG
49010.0
75
```

Esta saída mostra que nossa classe criada manualmente funciona como uma classe criada usando a sintaxe padrão do Python. Demonstra que uma classe é fundamentalmente apenas um nome, uma tupla de classes base e um dicionário de métodos e atributos. A função `type()` simplesmente constrói um objeto de classe a partir desses componentes.

Saia do shell do Python quando terminar:

```python
exit()
```
