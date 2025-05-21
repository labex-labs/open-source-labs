# Criando Objetos Somente Leitura com Proxies

Nesta etapa, vamos explorar classes proxy, um padrão muito útil em Python. As classes proxy permitem que você pegue um objeto existente e altere seu comportamento sem alterar seu código original. Isso é como colocar um wrapper especial em torno de um objeto para adicionar novos recursos ou restrições.

## O que é um Proxy?

Um proxy é um objeto que fica entre você e outro objeto. Ele tem o mesmo conjunto de funções e propriedades que o objeto original, mas pode fazer coisas extras. Por exemplo, ele pode controlar quem pode acessar o objeto, manter um registro de ações (logging) ou adicionar outros recursos úteis.

Vamos criar um proxy somente leitura. Esse tipo de proxy impedirá que você altere os atributos de um objeto.

### Passo 1: Crie a Classe Proxy Somente Leitura

Primeiro, precisamos criar um arquivo Python que defina nosso proxy somente leitura.

1. Navegue até o diretório `/home/labex/project`.
2. Crie um novo arquivo chamado `readonly_proxy.py` neste diretório.
3. Abra o arquivo `readonly_proxy.py` e adicione o seguinte código:

```python
class ReadonlyProxy:
    def __init__(self, obj):
        # Store the wrapped object directly in __dict__ to avoid triggering __setattr__
        self.__dict__['_obj'] = obj

    def __getattr__(self, name):
        # Forward attribute access to the wrapped object
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # Block all attribute assignments
        raise AttributeError("Cannot modify a read-only object")
```

Neste código, a classe `ReadonlyProxy` é definida. O método `__init__` armazena o objeto que queremos encapsular. Usamos `self.__dict__` para armazená-lo diretamente para evitar chamar o método `__setattr__`. O método `__getattr__` é usado quando tentamos acessar um atributo do proxy. Ele simplesmente passa a solicitação para o objeto encapsulado. O método `__setattr__` é chamado quando tentamos alterar um atributo. Ele levanta um erro para evitar quaisquer alterações.

### Passo 2: Crie um Arquivo de Teste

Agora, criaremos um arquivo de teste para ver como nosso proxy somente leitura funciona.

1. Crie um novo arquivo chamado `test_readonly.py` no mesmo diretório `/home/labex/project`.
2. Adicione o seguinte código ao arquivo `test_readonly.py`:

```python
from stock import Stock
from readonly_proxy import ReadonlyProxy

# Create a normal Stock object
stock = Stock('AAPL', 100, 150.75)
print("Original stock object:")
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")
print(f"Cost: {stock.cost}")

# Modify the original stock object
stock.shares = 200
print(f"\nAfter modification - Shares: {stock.shares}")
print(f"After modification - Cost: {stock.cost}")

# Create a read-only proxy around the stock
readonly_stock = ReadonlyProxy(stock)
print("\nRead-only proxy object:")
print(f"Name: {readonly_stock.name}")
print(f"Shares: {readonly_stock.shares}")
print(f"Price: {readonly_stock.price}")
print(f"Cost: {readonly_stock.cost}")

# Try to modify the read-only proxy
try:
    print("\nAttempting to modify the read-only proxy...")
    readonly_stock.shares = 300
except AttributeError as e:
    print(f"Error: {e}")

# Show that the original object is unchanged
print(f"\nOriginal stock shares are still: {stock.shares}")
```

Neste código de teste, primeiro criamos um objeto `Stock` normal e imprimimos suas informações. Em seguida, modificamos um de seus atributos e imprimimos as informações atualizadas. Em seguida, criamos um proxy somente leitura para o objeto `Stock` e imprimimos suas informações. Finalmente, tentamos modificar o proxy somente leitura e esperamos obter um erro.

### Passo 3: Execute o Script de Teste

Depois de criar a classe proxy e o arquivo de teste, precisamos executar o script de teste para ver os resultados.

1. Abra um terminal e navegue até o diretório `/home/labex/project` usando o seguinte comando:

```bash
cd /home/labex/project
```

2. Execute o script de teste usando o seguinte comando:

```bash
python3 test_readonly.py
```

Você deve ver uma saída semelhante a:

```
Original stock object:
Name: AAPL
Shares: 100
Price: 150.75
Cost: 15075.0

After modification - Shares: 200
After modification - Cost: 30150.0

Read-only proxy object:
Name: AAPL
Shares: 200
Price: 150.75
Cost: 30150.0

Attempting to modify the read-only proxy...
Error: Cannot modify a read-only object

Original stock shares are still: 200
```

## Como o Proxy Funciona

A classe `ReadonlyProxy` usa dois métodos especiais para alcançar sua funcionalidade somente leitura:

1. `__getattr__(self, name)`: Este método é chamado quando o Python não consegue encontrar um atributo da maneira normal. Em nossa classe `ReadonlyProxy`, usamos a função `getattr()` para passar a solicitação de acesso ao atributo para o objeto encapsulado. Portanto, quando você tenta acessar um atributo do proxy, ele realmente obterá o atributo do objeto encapsulado.

2. `__setattr__(self, name, value)`: Este método é chamado quando você tenta atribuir um valor a um atributo. Em nossa implementação, levantamos um `AttributeError` para impedir que quaisquer alterações sejam feitas nos atributos do proxy.

3. No método `__init__`, modificamos diretamente `self.__dict__` para armazenar o objeto encapsulado. Isso é importante porque, se usássemos a maneira normal de atribuir o objeto, ele chamaria o método `__setattr__`, que levantaria um erro.

Este padrão de proxy nos permite adicionar uma camada somente leitura em torno de qualquer objeto existente sem alterar sua classe original. O objeto proxy age como o objeto encapsulado, mas não permitirá que você faça nenhuma modificação.
