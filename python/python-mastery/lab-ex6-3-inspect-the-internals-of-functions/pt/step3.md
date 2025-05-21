# Aplicando a Inspeção de Funções em Classes

Agora, vamos pegar o que aprendemos sobre inspeção de funções e usá-lo para melhorar a implementação de uma classe. A inspeção de funções nos permite olhar para dentro das funções e entender sua estrutura, como os parâmetros que elas recebem. Neste caso, vamos usá-la para tornar nosso código de classe mais eficiente e menos propenso a erros. Vamos modificar uma classe `Structure` para que ela possa detectar automaticamente os nomes dos campos a partir da assinatura do método `__init__`.

## Entendendo a Classe Structure

O arquivo `structure.py` contém uma classe `Structure`. Esta classe atua como uma classe base, o que significa que outras classes podem herdar dela para criar objetos de dados estruturados. Atualmente, para definir os atributos dos objetos criados a partir de classes que herdam de `Structure`, precisamos definir uma variável de classe `_fields`.

Vamos abrir o arquivo no editor. Usaremos o seguinte comando para navegar até o diretório do projeto:

```bash
cd ~/project
```

Depois de executar este comando, você pode encontrar e visualizar a classe `Structure` existente no arquivo `structure.py` dentro do WebIDE.

## Criando uma Classe Stock

Vamos criar uma classe `Stock` que herda da classe `Structure`. Herança significa que a classe `Stock` obterá todos os recursos da classe `Structure` e também poderá adicionar os seus próprios. Adicionaremos o seguinte código ao final do arquivo `structure.py`:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()
```

No entanto, há um problema com essa abordagem. Precisamos definir tanto a tupla `_fields` quanto o método `__init__` com os mesmos nomes de parâmetros. Isso é redundante porque estamos essencialmente escrevendo a mesma informação duas vezes. Se esquecermos de atualizar um quando alteramos o outro, isso pode levar a erros.

## Adicionando um Método de Classe set_fields

Para corrigir esse problema, adicionaremos um método de classe `set_fields` à classe `Structure`. Este método detectará automaticamente os nomes dos campos a partir da assinatura `__init__`. Aqui está o código que precisamos adicionar à classe `Structure`:

```python
@classmethod
def set_fields(cls):
    # Get the signature of the __init__ method
    import inspect
    sig = inspect.signature(cls.__init__)

    # Get parameter names, skipping 'self'
    params = list(sig.parameters.keys())[1:]

    # Set _fields attribute on the class
    cls._fields = tuple(params)
```

Este método usa o módulo `inspect`, que é uma ferramenta poderosa em Python para obter informações sobre objetos como funções e classes. Primeiro, ele obtém a assinatura do método `__init__`. Em seguida, ele extrai os nomes dos parâmetros, mas ignora o parâmetro `self` porque `self` é um parâmetro especial em classes Python que se refere à própria instância. Finalmente, ele define a variável de classe `_fields` com esses nomes de parâmetros.

## Modificando a Classe Stock

Agora que temos o método `set_fields`, podemos simplificar nossa classe `Stock`. Substitua o código anterior da classe `Stock` pelo seguinte:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

# Call set_fields to automatically set _fields from __init__
Stock.set_fields()
```

Dessa forma, não precisamos definir manualmente a tupla `_fields`. O método `set_fields` cuidará disso para nós.

## Testando a Classe Modificada

Para garantir que nossa classe modificada funcione corretamente, criaremos um script de teste simples. Crie um novo arquivo chamado `test_structure.py` e adicione o seguinte código:

```python
from structure import Stock

def test_stock():
    # Create a Stock object
    s = Stock(name='GOOG', shares=100, price=490.1)

    # Test string representation
    print(f"Stock representation: {s}")

    # Test attribute access
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")

    # Test attribute modification
    s.shares = 50
    print(f"Updated shares: {s.shares}")

    # Test attribute error
    try:
        s.share = 50  # Misspelled attribute
        print("Error: Did not raise AttributeError")
    except AttributeError as e:
        print(f"Correctly raised: {e}")

if __name__ == "__main__":
    test_stock()
```

Este script de teste cria um objeto `Stock`, testa sua representação de string, acessa seus atributos, modifica um atributo e tenta acessar um atributo com erro de ortografia para verificar se ele gera o erro correto.

Para executar o script de teste, use o seguinte comando:

```bash
python3 test_structure.py
```

Você deve ver uma saída semelhante a esta:

```
Stock representation: Stock('GOOG',100,490.1)
Name: GOOG
Shares: 100
Price: 490.1
Updated shares: 50
Correctly raised: No attribute share
```

## Como Funciona

1. O método `set_fields` usa `inspect.signature()` para obter os nomes dos parâmetros do método `__init__`. Esta função nos dá informações detalhadas sobre os parâmetros do método `__init__`.
2. Em seguida, ele define automaticamente a variável de classe `_fields` com base nesses nomes de parâmetros. Portanto, não precisamos escrever os mesmos nomes de parâmetros em dois lugares diferentes.
3. Isso elimina a necessidade de definir manualmente tanto `_fields` quanto `__init__` com nomes de parâmetros correspondentes. Isso torna nosso código mais fácil de manter, porque se alterarmos os parâmetros no método `__init__`, o `_fields` será atualizado automaticamente.

Essa abordagem usa a inspeção de funções para tornar nosso código mais fácil de manter e menos propenso a erros. É uma aplicação prática dos recursos de introspecção do Python, que nos permitem examinar e modificar objetos em tempo de execução.
