# Criando a Classe Stock

Em Python, uma classe é um modelo para criar objetos. Ela permite que você agrupe dados e funcionalidades. Agora, vamos criar nossa classe `Stock` para representar informações de ações. Uma ação tem certas características, como seu nome, o número de ações e o preço por ação. Definiremos atributos para esses aspectos dentro de nossa classe.

1. Primeiro, você precisa estar no diretório correto no WebIDE. Se você ainda não estiver no diretório `/home/labex/project`, navegue até ele. É aqui que trabalharemos no código da nossa classe `Stock`.

2. Depois de estar no diretório certo, crie um novo arquivo no editor. Nomeie este arquivo `stock.py`. Este arquivo conterá o código para nossa classe `Stock`.

3. Agora, vamos adicionar o código para definir a classe `Stock`. Copie e cole o seguinte código no arquivo `stock.py`:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

Neste código:

- A declaração `class Stock:` cria uma nova classe chamada `Stock`. Isso é como um modelo para criar objetos de ações.
- O método `__init__` é um método especial em classes Python. Ele é chamado de construtor. Quando você cria um novo objeto da classe `Stock`, o método `__init__` será executado automaticamente. Ele recebe três parâmetros: `name`, `shares` e `price`. Esses parâmetros representam as informações sobre a ação.
- Dentro do método `__init__`, usamos `self` para nos referir à instância da classe. Armazenamos os valores dos parâmetros como atributos de instância. Por exemplo, `self.name = name` armazena o parâmetro `name` como um atributo do objeto.
- O método `cost()` é um método personalizado que definimos. Ele calcula o custo total da ação multiplicando o número de ações (`self.shares`) pelo preço por ação (`self.price`).

4. Depois de adicionar o código, salve o arquivo. Você pode fazer isso pressionando `Ctrl+S` ou clicando no ícone Salvar. Salvar o arquivo garante que suas alterações sejam preservadas.

Vamos examinar o código novamente para garantir que o entendemos:

- Definimos uma classe chamada `Stock`. Esta classe será usada para criar objetos de ações.
- O método `__init__` recebe três parâmetros: `name`, `shares` e `price`. Ele inicializa os atributos do objeto com esses valores.
- Dentro de `__init__`, armazenamos esses parâmetros como atributos de instância usando `self`. Isso permite que cada objeto tenha seu próprio conjunto de valores para esses atributos.
- Adicionamos um método `cost()` que calcula o custo total multiplicando as ações pelo preço. Esta é uma funcionalidade útil para nossos objetos de ações.

Quando criamos um objeto `Stock`, o método `__init__` será executado automaticamente, configurando o estado inicial do nosso objeto com os valores que fornecemos. Dessa forma, podemos facilmente criar vários objetos de ações com diferentes nomes, números de ações e preços.
