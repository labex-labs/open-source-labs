# Agregando iteración a clases personalizadas

Ahora que has comprendido los conceptos básicos de los generadores, vamos a utilizarlos para agregar capacidades de iteración a clases personalizadas. En Python, si quieres hacer que una clase sea iterable, debes implementar el método especial `__iter__()`. Una clase iterable te permite recorrer sus elementos, al igual que puedes recorrer una lista o una tupla. Esta es una característica poderosa que hace que tus clases personalizadas sean más flexibles y fáciles de manejar.

## Comprendiendo el método `__iter__()`

El método `__iter__()` es una parte crucial para hacer que una clase sea iterable. Debe devolver un objeto iterador. Un iterador es un objeto sobre el que se puede iterar (recorrer en un bucle). Una forma simple y efectiva de lograr esto es definir `__iter__()` como una función generadora. Una función generadora utiliza la palabra clave `yield` para producir una secuencia de valores uno a la vez. Cada vez que se encuentra la declaración `yield`, la función se pausa y devuelve el valor. La próxima vez que se llame al iterador, la función se reanuda desde donde se dejó.

## Modificando la clase Structure

En la configuración de este laboratorio, proporcionamos una clase base `Structure`. Otras clases, como `Stock`, pueden heredar de esta clase `Structure`. La herencia es una forma de crear una nueva clase que hereda las propiedades y métodos de una clase existente. Al agregar un método `__iter__()` a la clase `Structure`, podemos hacer que todas sus subclases sean iterables. Esto significa que cualquier clase que herede de `Structure` tendrá automáticamente la capacidad de ser recorrida en un bucle.

1. Abre el archivo `structure.py` en el WebIDE:

```bash
cd ~/project
```

Este comando cambia el directorio de trabajo actual al directorio `project` donde se encuentra el archivo `structure.py`. Debes estar en el directorio correcto para acceder y modificar el archivo.

2. Observa la implementación actual de la clase `Structure`:

```python
class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)
```

La clase `Structure` tiene una lista `_fields` que almacena los nombres de los atributos. El método `__init__()` es el constructor de la clase. Inicializa los atributos del objeto comprobando si el número de argumentos pasados es igual al número de campos. Si no lo es, levanta una excepción `TypeError`. De lo contrario, establece los atributos utilizando la función `setattr()`.

3. Agrega un método `__iter__()` que produzca cada valor de atributo en orden:

```python
def __iter__(self):
    for name in self._fields:
        yield getattr(self, name)
```

Este método `__iter__()` es una función generadora. Recorre la lista `_fields` y utiliza la función `getattr()` para obtener el valor de cada atributo. La palabra clave `yield` devuelve entonces el valor uno por uno.

El archivo `structure.py` completo ahora debería verse así:

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
```

Esta clase `Structure` actualizada ahora tiene el método `__iter__()`, lo que la hace y a sus subclases iterables.

4. Guarda el archivo.
   Después de realizar cambios en el archivo `structure.py`, debes guardarlo para que los cambios se apliquen.

5. Ahora probemos la capacidad de iteración creando una instancia de `Stock` y recorriéndola:

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('Iterating over Stock:'); [print(val) for val in s]"
```

Este comando crea una instancia de la clase `Stock`, que hereda de la clase `Structure`. Luego recorre la instancia utilizando una comprensión de lista e imprime cada valor.

Deberías ver una salida como esta:

```
Iterating over Stock:
GOOG
100
490.1
```

Ahora cualquier clase que herede de `Structure` será automáticamente iterable, y la iteración producirá los valores de los atributos en el orden definido por la lista `_fields`. Esto significa que puedes recorrer fácilmente los atributos de cualquier subclase de `Structure` sin tener que escribir código adicional para la iteración.
