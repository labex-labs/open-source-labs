# Atributos Privados

Qualquer nome de atributo com um `_` inicial é considerado _privado_.

```python
class Person(object):
    def __init__(self, name):
        self._name = 0
```

Como mencionado anteriormente, isso é apenas um estilo de programação. Você ainda pode acessá-lo e alterá-lo.

```python
>>> p = Person('Guido')
>>> p._name
'Guido'
>>> p._name = 'Dave'
>>>
```

Como regra geral, qualquer nome com um `_` inicial é considerado uma implementação interna, seja uma variável, uma função ou um nome de módulo. Se você se encontrar usando esses nomes diretamente, provavelmente está fazendo algo errado. Procure por funcionalidades de nível superior.
