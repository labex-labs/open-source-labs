# Atributos privados

Cualquier nombre de atributo que comience con `_` se considera _privado_.

```python
class Person(object):
    def __init__(self, name):
        self._name = 0
```

Como se mencionó anteriormente, esto es solo un estilo de programación. Aún puedes acceder y cambiarlo.

```python
>>> p = Person('Guido')
>>> p._name
'Guido'
>>> p._name = 'Dave'
>>>
```

Como regla general, cualquier nombre que comience con `_` se considera parte de la implementación interna, ya sea que se trate de una variable, una función o un nombre de módulo. Si te encuentras usando directamente tales nombres, probablemente estás haciendo algo mal. Busca una funcionalidad de mayor nivel.
