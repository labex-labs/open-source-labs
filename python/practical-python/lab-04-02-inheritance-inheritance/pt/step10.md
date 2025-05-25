# Classe base `object`

Se uma classe não tem pai, você às vezes vê `object` usado como a base.

```python
class Shape(object):
    ...
```

`object` é o pai de todos os objetos em Python.

\*Nota: tecnicamente não é obrigatório, mas você frequentemente o vê especificado como uma herança de seu uso obrigatório no Python 2. Se omitido, a classe ainda herda implicitamente de `object`.
