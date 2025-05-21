# Desafio: Usando um Objeto Chamável como um Método

Em Python, quando você usa um objeto chamável como um método dentro de uma classe, há um desafio único que você precisa enfrentar. Um objeto chamável é algo que você pode "chamar" como uma função, como uma função em si ou um objeto com um método `__call__`. Quando usado como um método de classe, nem sempre funciona como esperado devido à forma como o Python passa a instância (`self`) como o primeiro argumento.

Vamos explorar esse problema criando uma classe `Stock`. Esta classe representará uma ação com atributos como nome, número de ações e preço. Também usaremos um validador para garantir que os dados com os quais estamos trabalhando estejam corretos.

Primeiro, abra o arquivo `stock.py` para começar a escrever nossa classe `Stock`. Você pode usar o seguinte comando para abrir o arquivo em um editor:

```bash
code /home/labex/project/stock.py
```

Agora, adicione o seguinte código ao arquivo `stock.py`. Este código define a classe `Stock` com um método `__init__` para inicializar os atributos da ação, uma propriedade `cost` para calcular o custo total e um método `sell` para reduzir o número de ações. Também tentaremos usar o `ValidatedFunction` para validar a entrada para o método `sell`.

```python
from validate import ValidatedFunction, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        self.shares -= nshares

    # Try to use ValidatedFunction
    sell = ValidatedFunction(sell)
```

Depois de definir a classe `Stock`, precisamos testá-la para ver se ela funciona como esperado. Crie um arquivo de teste chamado `test_stock.py` e abra-o usando o seguinte comando:

```bash
code /home/labex/project/test_stock.py
```

Adicione o seguinte código ao arquivo `test_stock.py`. Este código cria uma instância da classe `Stock`, imprime o número inicial de ações e o custo, tenta vender algumas ações e, em seguida, imprime o número atualizado de ações e o custo.

```python
from stock import Stock

try:
    # Create a stock
    s = Stock('GOOG', 100, 490.1)

    # Get the initial cost
    print(f"Initial shares: {s.shares}")
    print(f"Initial cost: ${s.cost}")

    # Try to sell some shares
    s.sell(10)

    # Check the updated cost
    print(f"After selling, shares: {s.shares}")
    print(f"After selling, cost: ${s.cost}")

except Exception as e:
    print(f"Error: {e}")
```

Agora, execute o arquivo de teste usando o seguinte comando:

```bash
python3 /home/labex/project/test_stock.py
```

Você provavelmente encontrará um erro semelhante a:

```
Error: missing a required argument: 'nshares'
```

Este erro ocorre porque, quando o Python chama um método como `s.sell(10)`, ele realmente chama `Stock.sell(s, 10)` nos bastidores. O parâmetro `self` representa a instância da classe e é automaticamente passado como o primeiro argumento. No entanto, nosso `ValidatedFunction` não lida com este parâmetro `self` corretamente porque não sabe que está sendo usado como um método.

**Entendendo o Problema**

Quando você define um método dentro de uma classe e, em seguida, o substitui por um `ValidatedFunction`, você está essencialmente envolvendo o método original. O problema é que o método envolvido não lida automaticamente com o parâmetro `self` corretamente. Ele espera os argumentos de uma forma que não leva em consideração a instância sendo passada como o primeiro argumento.

**Corrigindo o Problema**

Para corrigir esse problema, precisamos modificar a maneira como lidamos com os métodos. Criaremos uma nova classe chamada `ValidatedMethod` que pode lidar com chamadas de método corretamente. Adicione o seguinte código ao final do arquivo `validate.py`:

```python
import inspect

class ValidatedMethod:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __get__(self, instance, owner):
        # This method is called when the attribute is accessed as a method
        if instance is None:
            return self

        # Return a callable that binds 'self' to the instance
        def method_wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return method_wrapper

    def __call__(self, instance, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(instance, *args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(instance, *args, **kwargs)
```

Agora, precisamos modificar a classe `Stock` para usar `ValidatedMethod` em vez de `ValidatedFunction`. Abra o arquivo `stock.py` novamente:

```bash
code /home/labex/project/stock.py
```

Atualize a classe `Stock` da seguinte forma:

```python
from validate import ValidatedMethod, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @ValidatedMethod
    def sell(self, nshares: Integer):
        self.shares -= nshares
```

A classe `ValidatedMethod` é um descritor (descriptor), que é um tipo especial de objeto em Python que pode alterar como os atributos são acessados. O método `__get__` é chamado quando o atributo é acessado como um método. Ele retorna um chamável que passa corretamente a instância como o primeiro argumento.

Execute o arquivo de teste novamente usando o seguinte comando:

```bash
python3 /home/labex/project/test_stock.py
```

Agora você deve ver uma saída semelhante a:

```
Initial shares: 100
Initial cost: $49010.0
After selling, shares: 90
After selling, cost: $44109.0
```

Este desafio mostrou a você um aspecto importante dos objetos chamáveis. Ao usá-los como métodos em uma classe, eles exigem um tratamento especial. Ao implementar o protocolo de descritor com o método `__get__`, podemos criar objetos chamáveis que funcionam corretamente tanto como funções independentes quanto como métodos.
