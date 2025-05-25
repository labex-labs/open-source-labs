# Exercício 2.19: Compreensões de Lista

Experimente algumas compreensões de lista simples apenas para se familiarizar com a sintaxe.

```python
>>> nums = [1,2,3,4]
>>> squares = [ x * x for x in nums ]
>>> squares
[1, 4, 9, 16]
>>> twice = [ 2 * x for x in nums if x > 2 ]
>>> twice
[6, 8]
>>>
```

Observe como as compreensões de lista estão criando uma nova lista com os dados devidamente transformados ou filtrados.
