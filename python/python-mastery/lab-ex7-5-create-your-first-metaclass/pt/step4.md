# Explorando a Herança de Metaclasses

As metaclasses têm uma característica fascinante: elas são "pegajosas". Isso significa que, uma vez que uma classe usa uma metaclasse, todas as suas subclasses na hierarquia de herança também usarão a mesma metaclasse. Em outras palavras, a propriedade da metaclasse se propaga pela cadeia de herança.

Vamos ver isso em ação:

1.  Primeiro, abra o arquivo `mymeta.py`. No final deste arquivo, vamos adicionar uma nova classe. Esta classe, chamada `MyStock`, herdará da classe `Stock`. O método `__init__` é usado para inicializar os atributos do objeto, e chamamos o método `__init__` da classe pai usando `super().__init__` para inicializar os atributos comuns. O método `info` é usado para retornar uma string formatada com informações sobre a ação. Adicione o seguinte código:

```python
class MyStock(Stock):
    def __init__(self, name, shares, price, category):
        super().__init__(name, shares, price)
        self.category = category

    def info(self):
        return f"{self.name} ({self.category}): {self.shares} shares at ${self.price}"
```

2.  Após adicionar o código, salve o arquivo `mymeta.py`. Salvar o arquivo garante que as alterações que fizemos sejam armazenadas e possam ser usadas posteriormente.

3.  Agora, criaremos um novo arquivo chamado `test_inheritance.py` para testar o comportamento de herança da metaclasse. Neste arquivo, importaremos a classe `MyStock` do arquivo `mymeta.py`. Em seguida, criaremos uma instância da classe `MyStock`, chamaremos seus métodos e imprimiremos os resultados para ver como a metaclasse funciona por meio da herança. Adicione o seguinte código a `test_inheritance.py`:

```python
# test_inheritance.py
from mymeta import MyStock

# Create a MyStock instance
tech_stock = MyStock("MSFT", 50, 305.75, "Technology")

# Test the methods
print(tech_stock.info())
print(f"Total cost: ${tech_stock.cost()}")

# Sell some shares
tech_stock.sell(5)
print(f"After selling: {tech_stock.shares} shares remaining")
print(f"Updated cost: ${tech_stock.cost()}")
```

4.  Finalmente, execute o arquivo `test_inheritance.py` para ver a metaclasse em ação por meio da herança. Abra seu terminal, navegue até o diretório onde o arquivo `test_inheritance.py` está localizado e execute o seguinte comando:

```bash
python3 test_inheritance.py
```

Você deve ver uma saída semelhante a:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Creating class : MyStock
Base classes   : (<class 'mymeta.Stock'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'info', '__doc__']
MSFT (Technology): 50 shares at $305.75
Total cost: $15287.5
After selling: 45 shares remaining
Updated cost: $13758.75
```

Observe que, embora não tenhamos especificado explicitamente uma metaclasse para a classe `MyStock`, a metaclasse ainda é aplicada. Isso demonstra claramente como as metaclasses se propagam por meio da herança.

## Usos Práticos de Metaclasses

Em nosso exemplo, a metaclasse simplesmente imprime informações sobre as classes. No entanto, as metaclasses têm muitas aplicações práticas na programação do mundo real:

1.  **Validação (Validation)**: Você pode usar metaclasses para verificar se uma classe possui os métodos ou atributos necessários. Isso ajuda a garantir que as classes atendam a certos critérios antes de serem usadas.
2.  **Registro (Registration)**: Metaclasses podem registrar classes automaticamente em um registro. Isso é útil quando você precisa acompanhar todas as classes de um determinado tipo.
3.  **Aplicação de interface (Interface enforcement)**: Elas podem ser usadas para garantir que as classes implementem as interfaces necessárias. Isso ajuda a manter uma estrutura consistente em seu código.
4.  **Programação orientada a aspectos (Aspect-oriented programming)**: Metaclasses podem adicionar comportamentos aos métodos. Por exemplo, você pode adicionar registro (logging) ou monitoramento de desempenho aos métodos sem modificar diretamente o código do método.
5.  **Sistemas ORM**: Em sistemas de Mapeamento Objeto-Relacional (ORM) como Django ou SQLAlchemy, as metaclasses são usadas para mapear classes para tabelas de banco de dados. Isso simplifica as operações de banco de dados em seu aplicativo.

As metaclasses são muito poderosas, mas devem ser usadas com moderação. Como Tim Peters (famoso pelo Zen of Python) disse uma vez, "Metaclasses são uma magia mais profunda do que 99% dos usuários deveriam se preocupar".
