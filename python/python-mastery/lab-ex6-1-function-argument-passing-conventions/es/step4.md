# Restringir nombres de atributos

Actualmente, nuestra clase `Structure` permite establecer cualquier atributo en sus instancias. Para los principiantes, esto puede parecer conveniente al principio, pero en realidad puede causar muchos problemas. Cuando trabajas con una clase, esperas que ciertos atributos estén presentes y se utilicen de una manera específica. Si los usuarios escriben mal el nombre de los atributos o intentan establecer atributos que no forman parte del diseño original, puede causar errores difíciles de encontrar.

## La necesidad de restringir atributos

Veamos un escenario simple para entender por qué necesitamos restringir los nombres de los atributos. Considera el siguiente código:

```python
s = Stock('GOOG', 100, 490.1)
s.shares = 50      # Correct attribute name
s.share = 60       # Typo in attribute name - creates a new attribute instead of updating
```

En la segunda línea, hay un error tipográfico. En lugar de `shares`, escribimos `share`. En Python, en lugar de generar un error, simplemente creará un nuevo atributo llamado `share`. Esto puede causar errores sutiles porque es posible que pienses que estás actualizando el atributo `shares`, pero en realidad estás creando uno nuevo. Esto puede hacer que tu código se comporte de manera inesperada y sea muy difícil de depurar.

## Implementar la restricción de atributos

Para resolver este problema, podemos sobrescribir el método `__setattr__`. Este método se llama cada vez que intentas establecer un atributo en un objeto. Al sobrescribirlo, podemos controlar qué atributos se pueden establecer y cuáles no.

Actualiza tu clase `Structure` en `structure.py` con el siguiente código:

```python
def __setattr__(self, name, value):
    """
    Restrict attribute setting to only those defined in _fields
    or attributes starting with underscore (private attributes).
    """
    if name.startswith('_'):
        # Allow setting private attributes (starting with '_')
        super().__setattr__(name, value)
    elif name in self._fields:
        # Allow setting attributes defined in _fields
        super().__setattr__(name, value)
    else:
        # Raise an error for other attributes
        raise AttributeError(f'No attribute {name}')
```

Así es cómo funciona este método:

1. Si el nombre del atributo comienza con un guión bajo (`_`), se considera un atributo privado. Los atributos privados se utilizan a menudo con fines internos en una clase. Permitimos que se establezcan estos atributos porque forman parte de la implementación interna de la clase.
2. Si el nombre del atributo está en la lista `_fields`, significa que es uno de los atributos definidos en el diseño de la clase. Permitimos que se establezcan estos atributos porque forman parte del comportamiento esperado de la clase.
3. Si el nombre del atributo no cumple con ninguna de estas condiciones, generamos un `AttributeError`. Esto le dice al usuario que está intentando establecer un atributo que no existe en la clase.

## Probar la restricción de atributos

Ahora que hemos implementado la restricción de atributos, probémosla para asegurarnos de que funciona como se espera. Crea un archivo llamado `test_attributes.py` con el siguiente código:

```python
# test_attributes.py
from structure import Stock

s = Stock('GOOG', 100, 490.1)

# This should work - valid attribute
print("Setting shares to 50")
s.shares = 50
print(f"Shares is now: {s.shares}")

# This should work - private attribute
print("\nSetting _internal_data")
s._internal_data = "Some data"
print(f"_internal_data is: {s._internal_data}")

# This should fail - invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.share = 60  # Typo in attribute name
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

Para ejecutar la prueba, abre tu terminal y escribe el siguiente comando:

```bash
python3 test_attributes.py
```

Deberías ver la siguiente salida:

```
Setting shares to 50
Shares is now: 50

Setting _internal_data
_internal_data is: Some data

Trying to set an invalid attribute:
Error correctly caught: No attribute share
```

Esta salida muestra que nuestra clase ahora evita errores accidentales de atributos. Permite establecer atributos válidos y atributos privados, pero genera un error cuando intentamos establecer un atributo inválido.

## El valor de la restricción de atributos

Restringir los nombres de los atributos es muy importante para escribir código robusto y mantenible. He aquí por qué:

1. Ayuda a detectar errores tipográficos en los nombres de los atributos. Si cometemos un error al escribir el nombre de un atributo, el código generará un error en lugar de crear un nuevo atributo. Esto facilita encontrar y corregir errores temprano en el proceso de desarrollo.
2. Evita intentos de establecer atributos que no existen en el diseño de la clase. Esto asegura que la clase se utilice como se pretendió y que el código se comporte de manera predecible.
3. Evita la creación accidental de nuevos atributos. La creación de nuevos atributos puede causar un comportamiento inesperado y dificultar la comprensión y el mantenimiento del código.

Al restringir los nombres de los atributos, hacemos que nuestro código sea más confiable y fácil de manejar.
