# Criando uma Classe de Ações Simples

Nesta etapa, vamos criar uma classe simples para representar uma ação. Entender como criar classes é fundamental em Python, pois nos permite modelar objetos do mundo real e seus comportamentos. Esta classe de ações simples será nosso ponto de partida para explorar como os objetos Python funcionam internamente.

Para começar, precisamos abrir um shell interativo do Python. O shell interativo do Python é um ótimo lugar para experimentar o código Python. Você pode digitar e executar comandos Python um por um. Para abri-lo, digite o seguinte comando no terminal:

```bash
python3
```

Depois de inserir o comando, você verá o prompt do Python (`>>>`). Isso indica que você está dentro do shell interativo do Python e pode começar a escrever código Python.

Agora, vamos definir uma classe `SimpleStock`. Uma classe em Python é como um projeto para criar objetos. Ela define os atributos (dados) e métodos (funções) que os objetos dessa classe terão. Veja como você define a classe `SimpleStock` com os atributos e métodos necessários:

```python
>>> class SimpleStock:
...     def __init__(self, name, shares, price):
...         self.name = name
...         self.shares = shares
...         self.price = price
...     def cost(self):
...         return self.shares * self.price
...
```

No código acima, o método `__init__` é um método especial nas classes Python. Ele é chamado de construtor e é usado para inicializar os atributos do objeto quando um objeto é criado. O parâmetro `self` se refere à instância da classe que está sendo criada. O método `cost` calcula o custo total das ações multiplicando o número de ações pelo preço por ação.

Depois de definir a classe, podemos criar instâncias da classe `SimpleStock`. Uma instância é um objeto real criado a partir do projeto da classe. Vamos criar duas instâncias para representar ações diferentes:

```python
>>> goog = SimpleStock('GOOG', 100, 490.10)
>>> ibm = SimpleStock('IBM', 50, 91.23)
```

Essas instâncias representam 100 ações da Google a $490,10 por ação e 50 ações da IBM a $91,23 por ação. Cada instância tem seu próprio conjunto de valores de atributo.

Vamos verificar se nossas instâncias estão funcionando corretamente. Podemos fazer isso verificando seus atributos e calculando seu custo. Isso nos ajudará a confirmar se a classe e seus métodos estão funcionando como esperado.

```python
>>> goog.name
'GOOG'
>>> goog.shares
100
>>> goog.price
490.1
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
```

O método `cost()` multiplica o número de ações pelo preço por ação para calcular o custo total de posse dessas ações. Ao executar esses comandos, podemos ver que as instâncias têm os valores de atributo corretos e que o método `cost` está calculando o custo com precisão.
