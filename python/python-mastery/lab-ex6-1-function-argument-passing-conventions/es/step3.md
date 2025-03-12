# Mejorar la representación de objetos

Nuestra clase `Structure` es útil para crear y acceder a objetos. Sin embargo, actualmente no tiene una buena forma de representarse como una cadena. Cuando imprimes un objeto o lo visualizas en el intérprete de Python, quieres ver una presentación clara e informativa. Esto te ayuda a entender qué es el objeto y cuáles son sus valores.

## Comprender la representación de objetos en Python

En Python, hay dos métodos especiales que se utilizan para representar objetos de diferentes maneras. Estos métodos son importantes porque te permiten controlar cómo se muestran tus objetos.

- `__str__` - Este método es utilizado por la función `str()` y la función `print()`. Proporciona una representación legible por humanos del objeto. Por ejemplo, si tienes un objeto `Stock`, el método `__str__` podría devolver algo como "Stock: GOOG, 100 shares at $490.1".
- `__repr__` - Este método es utilizado por el intérprete de Python y la función `repr()`. Da una representación más técnica y sin ambigüedades del objeto. El objetivo de `__repr__` es proporcionar una cadena que se pueda utilizar para recrear el objeto. Por ejemplo, para un objeto `Stock`, podría devolver "Stock('GOOG', 100, 490.1)".

Vamos a agregar un método `__repr__` a nuestra clase `Structure`. Esto hará que sea más fácil depurar nuestro código porque podemos ver claramente el estado de nuestros objetos.

## Implementar una buena representación

Ahora, necesitas actualizar tu archivo `structure.py`. Agregarás el método `__repr__` a la clase `Structure`. Este método creará una cadena que represente el objeto de una manera que se pueda utilizar para recrearlo.

```python
def __repr__(self):
    """
    Return a representation of the object that can be used to recreate it.
    Example: Stock('GOOG', 100, 490.1)
    """
    # Get the class name
    cls_name = type(self).__name__

    # Get all the field values
    values = [getattr(self, name) for name in self._fields]

    # Format the fields and values
    args_str = ', '.join(repr(value) for value in values)

    # Return the formatted string
    return f"{cls_name}({args_str})"
```

Esto es lo que hace este método paso a paso:

1. Obtiene el nombre de la clase utilizando `type(self).__name__`. Esto es importante porque te dice de qué tipo de objeto estás tratando.
2. Recupera todos los valores de los campos de la instancia. Esto te da los datos que el objeto contiene.
3. Crea una representación en cadena con el nombre de la clase y los valores. Esta cadena se puede utilizar para recrear el objeto.

## Probar la representación mejorada

Vamos a probar nuestra implementación mejorada. Crea un nuevo archivo llamado `test_repr.py`. Este archivo creará algunas instancias de nuestras clases e imprimirá sus representaciones.

```python
# test_repr.py
from structure import Stock, Point, Date

# Create instances
s = Stock('GOOG', 100, 490.1)
p = Point(3, 4)
d = Date(2023, 11, 9)

# Print the representations
print(repr(s))
print(repr(p))
print(repr(d))

# Direct printing also uses __repr__ in the interpreter
print(s)
print(p)
print(d)
```

Para ejecutar la prueba, abre tu terminal y escribe el siguiente comando:

```bash
python3 test_repr.py
```

Deberías ver la siguiente salida:

```
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
```

Esta salida es mucho más informativa que antes. Cuando ves `Stock('GOOG', 100, 490.1)`, inmediatamente sabes qué representa el objeto. Incluso podrías copiar esta cadena y usarla para recrear el objeto en tu código.

## El beneficio de buenas representaciones

Una buena implementación de `__repr__` es muy útil para la depuración. Cuando estás mirando objetos en el intérprete o registrando información durante la ejecución del programa, una representación clara facilita la identificación rápida de problemas. Puedes ver el estado exacto del objeto y entender qué podría estar saliendo mal.
