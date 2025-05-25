# Exercício 4.1: Objetos como Estruturas de Dados

Nas seções 2 e 3, trabalhamos com dados representados como tuplas e dicionários. Por exemplo, uma participação em ações poderia ser representada como uma tupla assim:

```python
s = ('GOOG',100,490.10)
```

ou como um dicionário assim:

```python
s = { 'name'   : 'GOOG',
      'shares' : 100,
      'price'  : 490.10
}
```

Você pode até escrever funções para manipular esses dados. Por exemplo:

```python
def cost(s):
    return s['shares'] * s['price']
```

No entanto, à medida que seu programa cresce, você pode querer criar um senso melhor de organização. Assim, outra abordagem para representar dados seria definir uma classe. Crie um arquivo chamado `stock.py` e defina uma classe `Stock` que represente uma única participação em ações. Faça com que as instâncias de `Stock` tenham atributos `name`, `shares` e `price`. Por exemplo:

```python
>>> import stock
>>> a = stock.Stock('GOOG',100,490.10)
>>> a.name
'GOOG'
>>> a.shares
100
>>> a.price
490.1
>>>
```

Crie mais alguns objetos `Stock` e manipule-os. Por exemplo:

```python
>>> b = stock.Stock('AAPL', 50, 122.34)
>>> c = stock.Stock('IBM', 75, 91.75)
>>> b.shares * b.price
6117.0
>>> c.shares * c.price
6881.25
>>> stocks = [a, b, c]
>>> stocks
[<stock.Stock object at 0x37d0b0>, <stock.Stock object at 0x37d110>, <stock.Stock object at 0x37d050>]
>>> for s in stocks:
     print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

... veja a saída ...
>>>
```

Uma coisa a enfatizar aqui é que a classe `Stock` age como uma fábrica para criar instâncias de objetos. Basicamente, você a chama como uma função e ela cria um novo objeto para você. Além disso, deve ser enfatizado que cada objeto é distinto - cada um tem seus próprios dados que são separados de outros objetos que foram criados.

Um objeto definido por uma classe é um pouco semelhante a um dicionário - apenas com uma sintaxe um pouco diferente. Por exemplo, em vez de escrever `s['name']` ou `s['price']`, você agora escreve `s.name` e `s.price`.
