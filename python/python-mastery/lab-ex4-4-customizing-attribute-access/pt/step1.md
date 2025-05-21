# Compreendendo `__setattr__` para Controle de Atributos

No Python, existem métodos especiais que permitem personalizar como os atributos de um objeto são acessados e modificados. Um desses métodos importantes é `__setattr__()`. Este método entra em ação toda vez que você tenta atribuir um valor a um atributo de um objeto. Ele oferece a capacidade de ter controle preciso sobre o processo de atribuição de atributos.

## O que é `__setattr__`?

O método `__setattr__(self, name, value)` atua como um interceptador para todas as atribuições de atributos. Quando você escreve uma simples instrução de atribuição como `obj.attr = value`, o Python não apenas atribui o valor diretamente. Em vez disso, ele internamente chama `obj.__setattr__("attr", value)`. Esse mecanismo fornece a você o poder de decidir o que deve acontecer durante a atribuição do atributo.

Agora, vamos ver um exemplo prático de como podemos usar `__setattr__` para restringir quais atributos podem ser definidos em uma classe.

### Passo 1: Crie um novo arquivo

Primeiro, abra um novo arquivo no WebIDE. Você pode fazer isso clicando no menu "File" e selecionando "New File". Nomeie este arquivo `restricted_stock.py` e salve-o no diretório `/home/labex/project`. Este arquivo conterá a definição da classe onde usaremos `__setattr__` para controlar a atribuição de atributos.

### Passo 2: Adicione código a `restricted_stock.py`

Adicione o seguinte código ao arquivo `restricted_stock.py`. Este código define uma classe `RestrictedStock`.

```python
class RestrictedStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __setattr__(self, name, value):
        # Only allow specific attributes
        if name not in {'name', 'shares', 'price'}:
            raise AttributeError(f'Cannot set attribute {name}')

        # If attribute is allowed, set it using the parent method
        super().__setattr__(name, value)
```

No método `__init__`, inicializamos o objeto com os atributos `name`, `shares` e `price`. O método `__setattr__` verifica se o nome do atributo que está sendo atribuído está no conjunto de atributos permitidos (`name`, `shares`, `price`). Se não estiver, ele levanta um `AttributeError`. Se o atributo for permitido, ele usa o método `__setattr__` da classe pai para realmente definir o atributo.

### Passo 3: Crie um arquivo de teste

Crie um novo arquivo chamado `test_restricted.py` e adicione o seguinte código a ele. Este código testará a funcionalidade da classe `RestrictedStock`.

```python
from restricted_stock import RestrictedStock

# Create a new stock
stock = RestrictedStock('GOOG', 100, 490.1)

# Test accessing existing attributes
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")

# Test modifying an existing attribute
print("\nChanging shares to 75...")
stock.shares = 75
print(f"New shares value: {stock.shares}")

# Test setting an invalid attribute
try:
    print("\nTrying to set an invalid attribute 'share'...")
    stock.share = 50
except AttributeError as e:
    print(f"Error: {e}")
```

Neste código, primeiro importamos a classe `RestrictedStock`. Em seguida, criamos uma instância da classe. Testamos o acesso a atributos existentes, a modificação de um atributo existente e, finalmente, tentamos definir um atributo inválido para ver se o método `__setattr__` funciona como esperado.

### Passo 4: Execute o arquivo de teste

Abra um terminal no WebIDE e execute os seguintes comandos para executar o arquivo `test_restricted.py`:

```bash
cd /home/labex/project
python3 test_restricted.py
```

Após executar esses comandos, você deverá ver uma saída semelhante a esta:

```
Name: GOOG
Shares: 100
Price: 490.1

Changing shares to 75...
New shares value: 75

Trying to set an invalid attribute 'share'...
Error: Cannot set attribute share
```

## Como Funciona

O método `__setattr__` em nossa classe `RestrictedStock` funciona nas seguintes etapas:

1. Primeiro, ele verifica se o nome do atributo está no conjunto permitido (`name`, `shares`, `price`).
2. Se o nome do atributo não estiver no conjunto permitido, ele levanta um `AttributeError`. Isso impede a atribuição de atributos indesejados.
3. Se o atributo for permitido, ele usa `super().__setattr__()` para realmente definir o atributo. Isso garante que o processo normal de atribuição de atributos ocorra para os atributos permitidos.

Este método é mais flexível do que usar `__slots__`, que vimos em exemplos anteriores. Embora `__slots__` possa otimizar o uso de memória e restringir atributos, ele tem limitações ao trabalhar com herança e pode entrar em conflito com outros recursos do Python. Nossa abordagem `__setattr__` nos dá controle semelhante sobre a atribuição de atributos sem algumas dessas limitações.
