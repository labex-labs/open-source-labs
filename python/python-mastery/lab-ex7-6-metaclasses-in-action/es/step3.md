# Creación de la metaclase StructureMeta

Ahora, hablemos de lo que vamos a hacer a continuación. Hemos encontrado una forma de recopilar todos los tipos de validadores. Nuestro siguiente paso es crear una metaclase. Pero, ¿qué es exactamente una metaclase? En Python, una metaclase es un tipo especial de clase. Sus instancias son clases en sí mismas. Esto significa que una metaclase puede controlar cómo se crea una clase. Puede gestionar el espacio de nombres donde se definen los atributos de la clase.

En nuestra situación, queremos crear una metaclase que haga disponibles los tipos de validadores cuando definamos una subclase de `Structure`. No queremos tener que importar estos tipos de validadores explícitamente cada vez.

Comencemos abriendo nuevamente el archivo `structure.py`. Puedes usar el siguiente comando para abrirlo:

```bash
code structure.py
```

Una vez abierto el archivo, necesitamos agregar algún código en la parte superior, antes de la definición de la clase `Structure`. Este código definirá nuestra metaclase.

```python
from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        """Prepare the namespace for the class being defined"""
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        """Create the new class using only the local namespace"""
        methods = methods.maps[0]  # Extract the local namespace
        return super().__new__(meta, name, bases, methods)
```

Ahora que hemos definido la metaclase, necesitamos modificar la clase `Structure` para usarla. De esta manera, cualquier clase que herede de `Structure` se beneficiará de la funcionalidad de la metaclase.

```python
class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

        # Set the remaining keyword arguments
        for name, val in kwargs.items():
            if name not in self._fields:
                raise TypeError(f'Invalid argument: {name}')
            setattr(self, name, val)

    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        args_str = ','.join(repr(val) for val in values)
        return f'{type(self).__name__}({args_str})'
```

Analicemos lo que hace este código:

1. El método `__prepare__()` es un método especial en Python. Se llama antes de que se cree la clase. Su función es preparar el espacio de nombres donde se definirán los atributos de la clase. Aquí usamos `ChainMap`. `ChainMap` es una herramienta útil que crea un diccionario en capas. En nuestro caso, incluye nuestros tipos de validadores, haciéndolos accesibles en el espacio de nombres de la clase.

2. El método `__new__()` es responsable de crear la nueva clase. Extraemos solo el espacio de nombres local, que es el primer diccionario en el `ChainMap`. Descartamos el diccionario de validadores porque ya hemos hecho que los tipos de validadores estén disponibles en el espacio de nombres.

Con esta configuración, cualquier clase que herede de `Structure` tendrá acceso a todos los tipos de validadores sin necesidad de importarlos explícitamente.

Ahora, probemos nuestra implementación. Crearemos una clase `Stock` utilizando nuestra clase base `Structure` mejorada.

```bash
cat > stock.py << EOF
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
EOF
```

Si nuestra metaclase está funcionando correctamente, deberíamos poder definir la clase `Stock` sin importar los tipos de validadores. Esto se debe a que la metaclase ya los ha hecho disponibles en el espacio de nombres.
