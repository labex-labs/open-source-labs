# Mejorando las clases con capacidades de iteración

Ahora, hemos hecho que nuestra clase `Structure` y sus subclases admitan la iteración. La iteración es un concepto poderoso en Python que te permite recorrer una colección de elementos uno por uno. Cuando una clase admite la iteración, se vuelve más flexible y puede trabajar con muchas características incorporadas de Python. Exploremos cómo este soporte para la iteración habilita muchas características poderosas en Python.

## Aprovechando la iteración para conversiones de secuencias

En Python, hay funciones incorporadas como `list()` y `tuple()`. Estas funciones son muy útiles porque pueden tomar cualquier objeto iterable como entrada. Un objeto iterable es algo sobre el que se puede iterar, como una lista, una tupla o, ahora, nuestras instancias de la clase `Structure`. Dado que nuestra clase `Structure` ahora admite la iteración, podemos convertir fácilmente sus instancias en listas o tuplas.

1. Intentemos estas operaciones con una instancia de `Stock`. La clase `Stock` es una subclase de `Structure`. Ejecuta el siguiente comando en tu terminal:

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('As list:', list(s)); print('As tuple:', tuple(s))"
```

Este comando primero importa la clase `Stock`, crea una instancia de ella y luego convierte esta instancia en una lista y una tupla utilizando las funciones `list()` y `tuple()` respectivamente. La salida mostrará la instancia representada como una lista y una tupla:

```
As list: ['GOOG', 100, 490.1]
As tuple: ('GOOG', 100, 490.1)
```

## Desempaquetado

Python tiene una característica muy útil llamada desempaquetado. El desempaquetado te permite tomar un objeto iterable y asignar sus elementos a variables individuales de una sola vez. Dado que nuestra instancia de `Stock` es iterable, podemos utilizar esta característica de desempaquetado en ella.

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); name, shares, price = s; print(f'Name: {name}, Shares: {shares}, Price: {price}')"
```

En este código, creamos una instancia de `Stock` y luego desempaquetamos sus elementos en tres variables: `name`, `shares` y `price`. Luego imprimimos estas variables. La salida mostrará los valores de estas variables:

```
Name: GOOG, Shares: 100, Price: 490.1
```

## Agregando capacidades de comparación

Cuando una clase admite la iteración, se vuelve más fácil implementar operaciones de comparación. Las operaciones de comparación se utilizan para verificar si dos objetos son iguales o no. Vamos a agregar un método `__eq__()` a nuestra clase `Structure` para comparar instancias.

1. Abre el archivo `structure.py` nuevamente. El método `__eq__()` es un método especial en Python que se llama cuando se utiliza el operador `==` para comparar dos objetos. Agrega el siguiente código a la clase `Structure` en el archivo `structure.py`:

```python
def __eq__(self, other):
    return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

Este método primero verifica si el objeto `other` es una instancia de la misma clase que `self` utilizando la función `isinstance()`. Luego convierte tanto `self` como `other` en tuplas y verifica si estas tuplas son iguales.

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

    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

2. Después de agregar el método `__eq__()`, guarda el archivo `structure.py`.

3. Probemos la capacidad de comparación. Ejecuta el siguiente comando en tu terminal:

```bash
python3 -c "from stock import Stock; a = Stock('GOOG', 100, 490.1); b = Stock('GOOG', 100, 490.1); c = Stock('AAPL', 200, 123.4); print(f'a == b: {a == b}'); print(f'a == c: {a == c}')"
```

Este código crea tres instancias de `Stock`: `a`, `b` y `c`. Luego compara `a` con `b` y `a` con `c` utilizando el operador `==`. La salida mostrará los resultados de estas comparaciones:

```
a == b: True
a == c: False
```

4. Ahora, para asegurarnos de que todo funcione correctamente, necesitamos ejecutar las pruebas unitarias. Las pruebas unitarias son un conjunto de código que verifican si diferentes partes de tu programa funcionan como se espera. Ejecuta el siguiente comando en tu terminal:

```bash
python3 teststock.py
```

Si todo funciona correctamente, deberías ver una salida que indique que las pruebas han pasado:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

Al agregar solo dos métodos simples (`__iter__()` y `__eq__()`), hemos mejorado significativamente nuestra clase `Structure` con capacidades que la hacen más "pythonica" y más fácil de usar.
