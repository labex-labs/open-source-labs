# Usando Sua Metaclasse

Agora, vamos criar uma classe que usa nossa metaclasse por meio de herança. Isso nos ajudará a entender como a metaclasse é chamada quando a classe é definida.

Uma metaclasse em Python é uma classe que cria outras classes. Quando você define uma classe, o Python usa uma metaclasse para construir esse objeto de classe. Ao usar a herança, podemos especificar qual metaclasse uma classe deve usar.

1.  Abra `mymeta.py` e adicione o seguinte código no final do arquivo:

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Aqui, estamos definindo uma classe `Stock` que herda de `myobject`. O método `__init__` é um método especial nas classes Python. Ele é chamado quando um objeto da classe é criado e é usado para inicializar os atributos do objeto. O método `cost` calcula o custo total da ação, e o método `sell` reduz o número de ações.

2.  Salve o arquivo pressionando Ctrl+S. Salvar o arquivo garante que as alterações que você fez sejam armazenadas e possam ser executadas posteriormente.

3.  Agora, vamos executar o arquivo para ver o que acontece. Abra um terminal no WebIDE e execute:

```bash
cd /home/labex/project
python3 mymeta.py
```

O comando `cd` altera o diretório de trabalho atual para `/home/labex/project`, e `python3 mymeta.py` executa o script Python `mymeta.py`.

Você deve ver uma saída semelhante a esta:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class '__main__.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
```

Essa saída mostra que nossa metaclasse está sendo invocada quando as classes `myobject` e `Stock` são criadas. Observe como:

- Para `Stock`, as classes base incluem `myobject` porque `Stock` herda de `myobject`.
- A lista de atributos inclui todos os métodos que definimos (`__init__`, `cost`, `sell`) junto com alguns atributos padrão.

4.  Vamos interagir com nossa classe `Stock`. Crie um novo arquivo chamado `test_stock.py` com o seguinte conteúdo:

```python
# test_stock.py
from mymeta import Stock

# Create a new Stock instance
apple = Stock("AAPL", 100, 154.50)

# Use the methods
print(f"Stock: {apple.name}, Shares: {apple.shares}, Price: ${apple.price}")
print(f"Total cost: ${apple.cost()}")

# Sell some shares
apple.sell(10)
print(f"After selling 10 shares: {apple.shares} shares remaining")
print(f"Updated cost: ${apple.cost()}")
```

Neste código, estamos importando a classe `Stock` do módulo `mymeta`. Em seguida, criamos uma instância da classe `Stock` chamada `apple`. Usamos os métodos da classe `Stock` para imprimir informações sobre a ação, calcular o custo total, vender algumas ações e, em seguida, imprimir as informações atualizadas.

5.  Execute este arquivo para testar nossa classe `Stock`:

```bash
python3 test_stock.py
```

Você deve ver uma saída como:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Stock: AAPL, Shares: 100, Price: $154.5
Total cost: $15450.0
After selling 10 shares: 90 shares remaining
Updated cost: $13905.0
```

Observe que nossas informações de metaclasse são impressas primeiro, seguido pela saída do nosso script de teste. Isso ocorre porque a metaclasse é invocada quando a classe é definida, o que acontece antes que o código no script de teste seja executado.
