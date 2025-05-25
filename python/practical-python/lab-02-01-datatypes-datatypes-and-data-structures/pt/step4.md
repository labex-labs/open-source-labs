# Tuplas

Uma tupla é uma coleção de valores agrupados.

Exemplo:

```python
s = ('GOOG', 100, 490.1)
```

Às vezes, os `()` são omitidos na sintaxe.

```python
s = 'GOOG', 100, 490.1
```

Casos especiais (0-tupla, 1-tupla).

```python
t = ()            # Uma tupla vazia
w = ('GOOG', )    # Uma tupla de 1 item
```

Tuplas são frequentemente usadas para representar registros ou estruturas _simples_. Tipicamente, é um único _objeto_ de múltiplas partes. Uma boa analogia: _Uma tupla é como uma única linha em uma tabela de banco de dados._

O conteúdo da tupla é ordenado (como um array).

```python
s = ('GOOG', 100, 490.1)
name = s[0]                 # 'GOOG'
shares = s[1]               # 100
price = s[2]                # 490.1
```

No entanto, o conteúdo não pode ser modificado.

```python
>>> s[1] = 75
TypeError: object does not support item assignment
```

Você pode, no entanto, criar uma nova tupla com base em uma tupla atual.

```python
s = (s[0], 75, s[2])
```
