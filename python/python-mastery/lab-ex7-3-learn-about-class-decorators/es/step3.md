# Aplicación de decoradores a través de la herencia

En el Paso 2, creamos un decorador de clase que simplifica nuestro código. Un decorador de clase es un tipo especial de función que toma una clase como argumento y devuelve una clase modificada. Es una herramienta útil en Python para agregar funcionalidad a las clases sin modificar su código original. Sin embargo, todavía necesitamos aplicar explícitamente el decorador `@validate_attributes` a cada clase. Esto significa que cada vez que creamos una nueva clase que necesita validación, tenemos que recordar agregar este decorador, lo cual puede ser un poco tedioso.

Podemos mejorar esto aún más aplicando el decorador automáticamente a través de la herencia. La herencia es un concepto fundamental en la programación orientada a objetos donde una subclase puede heredar atributos y métodos de una clase padre. El método `__init_subclass__` de Python se introdujo en Python 3.6 para permitir que las clases padre personalicen la inicialización de las subclases. Esto significa que cuando se crea una subclase, la clase padre puede realizar algunas acciones sobre ella. Podemos usar esta característica para aplicar automáticamente nuestro decorador a cualquier clase que herede de `Structure`.

Vamos a implementar esto:

1. Abre el archivo `structure.py`:

```bash
code ~/project/structure.py
```

Aquí, estamos usando el comando `code` para abrir el archivo `structure.py` en un editor de código. Este archivo contiene la definición de la clase `Structure`, y vamos a modificarla para usar el método `__init_subclass__`.

2. Agrega el método `__init_subclass__` a la clase `Structure`:

```python
class Structure:
    _fields = ()
    _types = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({values})'

    @classmethod
    def create_init(cls):
        '''
        Create an __init__ method from _fields
        '''
        body = 'def __init__(self, %s):\n' % ', '.join(cls._fields)
        for name in cls._fields:
            body += f'    self.{name} = {name}\n'

        # Execute the function creation code
        namespace = {}
        exec(body, namespace)
        setattr(cls, '__init__', namespace['__init__'])

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

El método `__init_subclass__` es un método de clase, lo que significa que se puede llamar en la propia clase en lugar de en una instancia de la clase. Cuando se crea una subclase de `Structure`, este método se llamará automáticamente. Dentro de este método, llamamos al decorador `validate_attributes` en la subclase `cls`. De esta manera, cada subclase de `Structure` tendrá automáticamente el comportamiento de validación.

3. Guarda el archivo.

Después de hacer cambios en el archivo `structure.py`, necesitamos guardarlo para que los cambios se apliquen.

4. Ahora, actualicemos nuestro archivo `stock.py` para aprovechar esta nueva característica:

```bash
code ~/project/stock.py
```

Estamos abriendo el archivo `stock.py` para modificarlo. Este archivo contiene la definición de la clase `Stock`, y vamos a hacer que herede de la clase `Structure` para usar la aplicación automática del decorador.

5. Modifica el archivo `stock.py` para eliminar el decorador explícito:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Ten en cuenta que:

- Eliminamos la importación de `validate_attributes` porque ya no necesitamos importarla explícitamente ya que el decorador se aplica automáticamente a través de la herencia.
- Eliminamos el decorador `@validate_attributes` porque el método `__init_subclass__` en la clase `Structure` se encargará de aplicarlo.
- El código ahora se basa únicamente en la herencia de `Structure` para obtener el comportamiento de validación.

6. Vuelve a ejecutar las pruebas para verificar que todo sigue funcionando:

```bash
cd ~/project
python3 teststock.py
```

Ejecutar las pruebas es importante para asegurarnos de que nuestros cambios no han roto nada. Si todas las pruebas pasan, significa que la aplicación automática del decorador a través de la herencia está funcionando correctamente.

Deberías ver que todas las pruebas pasan:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Probemos de nuevo nuestra clase `Stock` para asegurarnos de que funciona como se espera:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Este comando crea una instancia de la clase `Stock` e imprime su representación y el costo. Si la salida es como se espera, significa que la clase `Stock` está funcionando correctamente con la aplicación automática del decorador.

Salida:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

¡Esta implementación es aún más limpia! Al usar `__init_subclass__`, hemos eliminado la necesidad de aplicar explícitamente decoradores. Cualquier clase que herede de `Structure` obtiene automáticamente el comportamiento de validación.
