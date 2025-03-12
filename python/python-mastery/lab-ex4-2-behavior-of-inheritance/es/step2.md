# Construyendo un Sistema de Validación con Herencia

En este paso, vamos a construir un sistema de validación práctico utilizando herencia. La herencia es un concepto poderoso en la programación que te permite crear nuevas clases basadas en las existentes. De esta manera, puedes reutilizar código y crear programas más organizados y modulares. Al construir este sistema de validación, verás cómo se puede utilizar la herencia para crear componentes de código reutilizables que se pueden combinar de diferentes maneras.

## Creando la Clase Base de Validación

Primero, necesitamos crear una clase base para nuestros validadores. Para hacer esto, crearemos un nuevo archivo en el WebIDE. Así es como puedes hacerlo: haz clic en "Archivo" > "Nuevo Archivo", o puedes usar el atajo de teclado. Una vez que el nuevo archivo esté abierto, llámalo `validate.py`.

Ahora, agreguemos algo de código a este archivo para crear una clase base `Validator`. Esta clase servirá como la base para todos nuestros otros validadores.

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

En este código, hemos definido una clase `Validator` con un método `check`. El método `check` toma un valor como argumento y simplemente lo devuelve sin cambios. El decorador `@classmethod` se utiliza para hacer de este método un método de clase. Esto significa que podemos llamar a este método en la propia clase, sin tener que crear una instancia de la clase.

## Agregando Validadores de Tipo

A continuación, agregaremos algunos validadores que comprueben el tipo de un valor. Estos validadores heredarán de la clase `Validator` que acabamos de crear. Vuelve al archivo `validate.py` y agrega el siguiente código:

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

La clase `Typed` es una subclase de `Validator`. Tiene un atributo `expected_type`, que se establece inicialmente en `object`. El método `check` en la clase `Typed` comprueba si el valor dado es del tipo esperado. Si no lo es, levanta un `TypeError`. Si el tipo es correcto, llama al método `check` de la clase padre utilizando `super().check(value)`.

Las clases `Integer`, `Float` y `String` heredan de `Typed` y especifican el tipo exacto que deben comprobar. Por ejemplo, la clase `Integer` comprueba si un valor es un entero.

## Probando los Validadores de Tipo

Ahora que hemos creado nuestros validadores de tipo, probémoslos. Abre una nueva terminal y inicia el intérprete de Python ejecutando el siguiente comando:

```bash
python3
```

Una vez que el intérprete de Python esté en funcionamiento, podemos importar y probar nuestros validadores. Aquí hay un código para probarlos:

```python
from validate import Integer, String

Integer.check(10)  # Should return 10

try:
    Integer.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

String.check('10')  # Should return '10'
```

Cuando ejecutes este código, deberías ver algo como esto:

```
10
Error: Expected <class 'int'>
'10'
```

También podemos usar estos validadores en una función. Intentémoslo:

```python
def add(x, y):
    Integer.check(x)
    Integer.check(y)
    return x + y

add(2, 2)  # Should return 4

try:
    add('2', '3')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

Cuando ejecutes este código, deberías ver:

```
4
Error: Expected <class 'int'>
```

## Agregando Validadores de Valor

Hasta ahora, hemos creado validadores que comprueban el tipo de un valor. Ahora, agreguemos algunos validadores que comprueben el valor en sí en lugar del tipo. Vuelve al archivo `validate.py` y agrega el siguiente código:

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

El validador `Positive` comprueba si un valor es no negativo. Si el valor es menor que 0, levanta un `ValueError`. El validador `NonEmpty` comprueba si un valor tiene una longitud distinta de cero. Si la longitud es 0, levanta un `ValueError`.

## Componiendo Validadores con Herencia Múltiple

Ahora, vamos a combinar nuestros validadores utilizando herencia múltiple. La herencia múltiple permite que una clase herede de más de una clase padre. Vuelve al archivo `validate.py` y agrega el siguiente código:

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

Estas nuevas clases combinan la comprobación de tipo y la comprobación de valor. Por ejemplo, la clase `PositiveInteger` comprueba que un valor sea tanto un entero como no negativo. El orden de herencia es importante aquí. Los validadores se comprueban en el orden especificado en la definición de la clase.

## Probando los Validadores Compuestos

Probemos nuestros validadores compuestos. En el intérprete de Python, ejecuta el siguiente código:

```python
from validate import PositiveInteger, PositiveFloat, NonEmptyString

PositiveInteger.check(10)  # Should return 10

try:
    PositiveInteger.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    PositiveInteger.check(-10)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

NonEmptyString.check('hello')  # Should return 'hello'

try:
    NonEmptyString.check('')  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")
```

Cuando ejecutes este código, deberías ver:

```
10
Error: Expected <class 'int'>
Error: Expected >= 0
'hello'
Error: Must be non-empty
```

Esto muestra cómo podemos combinar validadores para crear reglas de validación más complejas.

Cuando hayas terminado de probar, puedes salir del intérprete de Python ejecutando el siguiente comando:

```python
exit()
```
