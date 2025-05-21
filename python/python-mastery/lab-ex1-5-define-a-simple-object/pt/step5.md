# Aprimorando a Classe de Ações

No Python, as classes são uma maneira poderosa de organizar dados e comportamento. Elas nos permitem agrupar dados e funções relacionadas. Nesta seção, aprimoraremos nossa classe `Stock` adicionando um método que exibe informações de ações formatadas. Este é um ótimo exemplo de como podemos encapsular dados e comportamento em nossas classes. Encapsulamento significa agrupar dados com os métodos que operam nesses dados, o que ajuda a manter nosso código organizado e mais fácil de gerenciar.

1. Primeiro, você precisa abrir o arquivo `stock.py` no editor do WebIDE. O arquivo `stock.py` é onde temos trabalhado em nossa classe `Stock`. Abri-lo no editor nos permite fazer alterações na definição da classe.

2. Agora, vamos modificar a classe `Stock` para adicionar um novo método `display()`. Este método será responsável por imprimir as informações da ação de uma maneira bem formatada. Veja como você pode fazer isso:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def display(self):
        print(f"Stock: {self.name}, Shares: {self.shares}, Price: ${self.price:.2f}, Total Cost: ${self.cost():.2f}")
```

No método `__init__`, inicializamos o nome da ação, o número de ações e o preço. O método `cost` calcula o custo total da ação multiplicando o número de ações pelo preço. O novo método `display` usa uma f-string para formatar e imprimir as informações da ação, incluindo o nome, número de ações, preço e custo total.

3. Depois de fazer essas alterações, você precisa salvar o arquivo. Você pode fazer isso pressionando `Ctrl+S` no seu teclado ou clicando no ícone Salvar no editor. Salvar o arquivo garante que suas alterações sejam preservadas e possam ser usadas posteriormente.

4. Em seguida, iniciaremos uma nova sessão interativa do Python. Uma sessão interativa nos permite testar nosso código imediatamente. Para iniciar a sessão, execute o seguinte comando no terminal:

```bash
python3 -i stock.py
```

A opção `-i` diz ao Python para iniciar uma sessão interativa após executar o arquivo `stock.py`. Dessa forma, podemos usar a classe `Stock` e seus métodos imediatamente.

5. Agora, vamos criar um objeto de ação e usar o novo método `display()`. Criaremos um objeto representando as ações da Apple e, em seguida, chamaremos o método `display` para ver as informações formatadas. Aqui está o código:

```python
apple = Stock('AAPL', 200, 154.50)
apple.display()
```

Quando você executar este código na sessão interativa, verá a seguinte saída:

```
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

Esta saída mostra que o método `display` está funcionando corretamente e está formatando as informações da ação conforme o esperado.

6. Finalmente, vamos criar uma lista de ações e exibi-las todas. Isso mostrará como podemos usar o método `display` com vários objetos de ações. Aqui está o código:

```python
stocks = [
    Stock('GOOG', 100, 490.10),
    Stock('IBM', 50, 91.50),
    Stock('AAPL', 200, 154.50)
]

for stock in stocks:
    stock.display()
```

Quando você executar este código, obterá a seguinte saída:

```
Stock: GOOG, Shares: 100, Price: $490.10, Total Cost: $49010.00
Stock: IBM, Shares: 50, Price: $91.50, Total Cost: $4575.00
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

Ao adicionar o método `display()` à nossa classe, encapsulamos a lógica de formatação dentro da própria classe. Isso torna nosso código mais organizado e mais fácil de manter. Se precisarmos alterar a forma como as informações da ação são exibidas, só precisamos modificar o método `display` em um só lugar, em vez de fazer alterações em todo o nosso código.
