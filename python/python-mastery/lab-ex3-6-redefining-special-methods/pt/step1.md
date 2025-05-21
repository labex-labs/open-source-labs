# Melhorando a Representação de Objetos com `__repr__`

Em Python, os objetos podem ser representados como strings de duas maneiras diferentes. Essas representações servem a propósitos diferentes e são úteis em vários cenários.

O primeiro tipo é a **representação de string**. Esta é criada pela função `str()`, que é chamada automaticamente quando você usa a função `print()`. A representação de string é projetada para ser legível por humanos. Ela apresenta o objeto em um formato que é fácil para nós entendermos e interpretarmos.

O segundo tipo é a **representação de código**. Esta é gerada pela função `repr()`. A representação de código mostra o código que você precisaria escrever para recriar o objeto. É mais sobre fornecer uma maneira precisa e inequívoca de representar o objeto em código.

Vamos olhar para um exemplo concreto usando a classe `date` embutida do Python. Isso ajudará você a ver a diferença entre as representações de string e código em ação.

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # Uses str()
2008-07-05
>>> d                     # Uses repr()
datetime.date(2008, 7, 5)
```

Neste exemplo, quando usamos `print(d)`, o Python chama a função `str()` no objeto `date` `d`, e obtemos uma data legível em formato `AAAA-MM-DD`. Quando simplesmente digitamos `d` no shell interativo, o Python chama a função `repr()`, e vemos o código necessário para recriar o objeto `date`.

Você pode obter explicitamente a string `repr()` de várias maneiras. Aqui estão alguns exemplos:

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
```

Agora, vamos aplicar esse conceito à nossa classe `Stock`. Vamos melhorar a classe implementando o método `__repr__`. Este método especial é chamado pelo Python quando ele precisa da representação de código de um objeto.

Para fazer isso, abra o arquivo `stock.py` em seu editor. Em seguida, adicione o método `__repr__` à classe `Stock`. O método `__repr__` deve retornar uma string que mostra o código necessário para recriar o objeto `Stock`.

```python
def __repr__(self):
    return f"Stock('{self.name}', {self.shares}, {self.price})"
```

Depois de adicionar o método `__repr__`, sua classe `Stock` completa agora deve se parecer com isto:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
```

Agora, vamos testar nossa classe `Stock` modificada. Abra um shell interativo do Python executando o seguinte comando em seu terminal:

```bash
python3
```

Depois que o shell interativo estiver aberto, tente os seguintes comandos:

```python
>>> import stock
>>> goog = stock.Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
```

Você também pode ver como o método `__repr__` funciona com um portfólio de ações. Aqui está um exemplo:

```python
>>> import reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
```

Como você pode ver, o método `__repr__` tornou nossos objetos `Stock` muito mais informativos quando exibidos no shell interativo ou no depurador. Agora ele mostra o código necessário para recriar cada objeto, o que é muito útil para depurar e entender o estado dos objetos.

Quando terminar de testar, você pode sair do interpretador Python executando o seguinte comando:

```python
>>> exit()
```
