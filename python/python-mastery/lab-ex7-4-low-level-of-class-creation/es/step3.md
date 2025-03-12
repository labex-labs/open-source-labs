# Generación eficiente de clases

Ahora que entiendes cómo crear clases utilizando la función `type()`, vamos a explorar una forma más eficiente de generar múltiples clases similares. Este método te ahorrará tiempo y reducirá la duplicación de código, haciendo que tu proceso de programación sea más fluido.

## Comprender las clases de validación actuales

Primero, necesitamos abrir el archivo `validate.py` en WebIDE. Este archivo ya contiene varias clases de validación, que se utilizan para comprobar si los valores cumplen con ciertas condiciones. Estas clases incluyen `Validator`, `Positive`, `PositiveInteger` y `PositiveFloat`. Vamos a agregar una clase base `Typed` y varios validadores específicos de tipo a este archivo.

Para abrir el archivo, ejecuta el siguiente comando en la terminal:

```bash
cd ~/project
```

## Agregar la clase de validación Typed

Comencemos agregando la clase de validación `Typed`. Esta clase se utilizará para comprobar si un valor es del tipo esperado.

```python
class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)
```

En este código, `expected_type` se establece en `object` por defecto. Las subclases lo reemplazarán con el tipo específico que están comprobando. El método `check` utiliza la función `isinstance` para comprobar si el valor es del tipo esperado. Si no lo es, genera un `TypeError`.

Tradicionalmente, crearíamos validadores específicos de tipo de esta manera:

```python
class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

Sin embargo, este enfoque es repetitivo. Podemos hacerlo mejor utilizando el constructor `type()` para generar estas clases de forma dinámica.

## Generar validadores de tipo de forma dinámica

Reemplazaremos las definiciones de clase individuales con un enfoque más eficiente.

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

Esto es lo que hace este código:

1. Define una lista de tuplas. Cada tupla contiene un nombre de clase y el tipo de Python correspondiente.
2. Utiliza una expresión generadora con la función `type()` para crear cada clase. La función `type()` toma tres argumentos: el nombre de la clase, una tupla de clases base y un diccionario de atributos de clase.
3. Utiliza `globals().update()` para agregar las clases recién creadas al espacio de nombres global. Esto hace que las clases sean accesibles en todo el módulo.

Tu archivo `validate.py` completo debería verse algo así:

```python
# Basic validator classes

class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

    @classmethod
    def check(cls, value):
        pass

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value <= 0:
            raise ValueError('Expected a positive value')
        super().check(value)

class PositiveInteger(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        super().check(value)

class PositiveFloat(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, float):
            raise TypeError('Expected a float')
        super().check(value)

class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)

# Generate type validators dynamically
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

## Probar las clases generadas dinámicamente

Ahora, probemos nuestras clases de validación generadas dinámicamente. Primero, abre una shell interactiva de Python.

```bash
cd ~/project
python3
```

Una vez que estés en la shell de Python, importa y prueba nuestros validadores.

```python
from validate import Integer, Float, String

# Test the Integer validator
i = Integer()
i.__set_name__(None, 'test_int')
try:
    i.check("not an integer")
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"Integer validation: {e}")

# Test the String validator
s = String()
s.__set_name__(None, 'test_str')
try:
    s.check(123)
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"String validation: {e}")

# Add a new validator class to the list
import sys
print("Current validator classes:", [cls for cls in dir() if cls in ['Integer', 'Float', 'String']])
```

Deberías ver una salida que muestre los errores de validación de tipo. Esto indica que nuestras clases generadas dinámicamente están funcionando correctamente.

Cuando termines de probar, sal de la shell de Python:

```python
exit()
```

## Expandir la generación dinámica de clases

Si quieres agregar más validadores de tipo, simplemente puedes actualizar la lista `_typed_classes` en `validate.py`.

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str),
    ('List', list),
    ('Dict', dict),
    ('Bool', bool)
]
```

Este enfoque proporciona una forma poderosa y eficiente de generar múltiples clases similares sin escribir código repetitivo. Te permite escalar fácilmente tu aplicación a medida que crecen tus requisitos.
