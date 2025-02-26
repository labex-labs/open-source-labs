# Ejercicio 4.1: Objetos como estructuras de datos

En las secciones 2 y 3, trabajamos con datos representados como tuplas y diccionarios. Por ejemplo, una posesión de acciones podría representarse como una tupla así:

```python
s = ('GOOG',100,490.10)
```

o como un diccionario así:

```python
s = { 'name'   : 'GOOG',
    'shares' : 100,
     'price'  : 490.10
}
```

Incluso puedes escribir funciones para manipular estos datos. Por ejemplo:

```python
def cost(s):
    return s['shares'] * s['price']
```

Sin embargo, a medida que tu programa crece, es posible que desees crear una mejor sensación de organización. Por lo tanto, otra forma de representar datos sería definir una clase. Crea un archivo llamado `stock.py` y define una clase `Stock` que represente una sola posesión de acciones. Haz que las instancias de `Stock` tengan atributos `name`, `shares` y `price`. Por ejemplo:

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

Crea algunos más objetos `Stock` y manipúlalos. Por ejemplo:

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

... mira la salida...
>>>
```

Una cosa que hay que enfatizar aquí es que la clase `Stock` actúa como una fábrica para crear instancias de objetos. Básicamente, la llamas como si fuera una función y te crea un nuevo objeto. Además, hay que enfatizar que cada objeto es distinto: cada uno tiene sus propios datos que son separados de otros objetos que se hayan creado.

Un objeto definido por una clase es algo similar a un diccionario, solo con una sintaxis un poco diferente. Por ejemplo, en lugar de escribir `s['name']` o `s['price']`, ahora se escribe `s.name` y `s.price`.
