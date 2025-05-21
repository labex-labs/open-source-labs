# Aplicando Validadores a uma Classe Stock

Nesta etapa, vamos ver como nossos validadores funcionam em uma situação do mundo real. Validadores são como pequenos verificadores que garantem que os dados que usamos atendam a certas regras. Criaremos uma classe `Stock`. Uma classe é como um modelo para criar objetos. Neste caso, a classe `Stock` representará uma ação no mercado de ações, e usaremos nossos validadores para garantir que os valores de seus atributos (como o número de ações e o preço) sejam válidos.

## Criando a Classe Stock

Primeiro, precisamos criar um novo arquivo. No WebIDE, crie um novo arquivo chamado `stock.py`. Este arquivo conterá o código para nossa classe `Stock`. Agora, adicione o seguinte código ao arquivo `stock.py`:

```python
# stock.py
from validate import PositiveInteger, PositiveFloat

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    def cost(self):
        return self.shares * self.price
```

Vamos detalhar o que este código faz:

1. Começamos importando os validadores `PositiveInteger` e `PositiveFloat` do nosso módulo `validate`. Esses validadores nos ajudarão a garantir que o número de ações seja um inteiro positivo e o preço seja um float positivo.
2. Em seguida, definimos uma classe `Stock`. Dentro da classe, temos um método `__init__`. Este método é chamado quando criamos um novo objeto `Stock`. Ele recebe três parâmetros: `name`, `shares` e `price`, e os atribui aos atributos do objeto.
3. Usamos propriedades e setters para validar os valores de `shares` e `price`. Uma propriedade é uma maneira de controlar o acesso a um atributo, e um setter é um método que é chamado quando tentamos definir o valor desse atributo. Quando definimos o atributo `shares`, o método `PositiveInteger.check` é chamado para garantir que o valor seja um inteiro positivo. Da mesma forma, quando definimos o atributo `price`, o método `PositiveFloat.check` é chamado para garantir que o valor seja um float positivo.
4. Finalmente, temos um método `cost`. Este método calcula o custo total da ação multiplicando o número de ações pelo preço.

## Testando a Classe Stock

Agora que criamos nossa classe `Stock`, precisamos testá-la para ver se os validadores estão funcionando corretamente. Abra um novo terminal e inicie o interpretador Python. Você pode fazer isso executando o seguinte comando:

```bash
python3
```

Depois que o interpretador Python estiver em execução, podemos importar e testar nossa classe `Stock`. Insira o seguinte código no interpretador Python:

```python
from stock import Stock

# Create a valid stock
s = Stock('GOOG', 100, 490.10)
print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try setting an invalid shares value
try:
    s.shares = -10
except ValueError as e:
    print(f"Error setting shares: {e}")

# Try setting an invalid price value
try:
    s.price = "not a price"
except TypeError as e:
    print(f"Error setting price: {e}")
```

Quando você executar este código, você deve ver uma saída semelhante à seguinte:

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Error setting shares: Expected >= 0
Error setting price: Expected <class 'float'>
```

Esta saída mostra que nossos validadores estão funcionando como esperado. A classe `Stock` não nos permite definir valores inválidos para `shares` e `price`. Quando tentamos definir um valor inválido, um erro é levantado, e podemos capturar e imprimir esse erro.

## Compreendendo Como a Herança Ajuda

Uma das grandes vantagens de usar nossos validadores é que podemos combinar facilmente diferentes regras de validação. Herança é um conceito poderoso em Python que nos permite criar novas classes com base em classes existentes. Com herança múltipla, podemos usar a função `super()` para chamar métodos de várias classes pai.

Por exemplo, se quisermos garantir que o nome da ação não esteja vazio, podemos seguir estas etapas:

1. Importe o validador `NonEmptyString` do módulo `validate`. Este validador nos ajudará a verificar se o nome da ação não é uma string vazia.
2. Adicione um setter de propriedade para o atributo `name` na classe `Stock`. Este setter usará o método `NonEmptyString.check()` para validar o nome da ação.

Isso mostra como a herança, especialmente a herança múltipla com a função `super()`, nos permite construir componentes que são flexíveis e podem ser reutilizados em diferentes combinações.

Quando terminar de testar, você pode sair do interpretador Python executando o seguinte comando:

```python
exit()
```
