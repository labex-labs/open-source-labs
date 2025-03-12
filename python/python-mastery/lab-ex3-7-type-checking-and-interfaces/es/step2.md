# Implementar una clase base abstracta

En este paso, vamos a convertir la clase `TableFormatter` en una clase base abstracta (ABC, por sus siglas en inglés) adecuada utilizando el módulo `abc` de Python. Pero primero, entendamos qué es una clase base abstracta y por qué la necesitamos.

## Comprender las clases base abstractas

Una clase base abstracta es un tipo especial de clase en Python. Es una clase de la que no se puede crear un objeto directamente, lo que significa que no se puede instanciar. El propósito principal de una clase base abstracta es definir una interfaz común para sus subclases. Establece un conjunto de reglas que todas las subclases deben seguir. Específicamente, requiere que las subclases implementen ciertos métodos.

Aquí hay algunos conceptos clave sobre las clases base abstractas:

- Usamos el módulo `abc` en Python para crear clases base abstractas.
- Los métodos marcados con el decorador `@abstractmethod` son como reglas. Cualquier subclase que herede de una clase base abstracta debe implementar estos métodos.
- Si intentas crear un objeto de una clase que hereda de una clase base abstracta pero no ha implementado todos los métodos requeridos, Python lanzará un error.

Ahora que entiendes los conceptos básicos de las clases base abstractas, veamos cómo podemos modificar la clase `TableFormatter` para que se convierta en una.

## Modificar la clase TableFormatter

Abre el archivo `tableformat.py`. Vamos a hacer algunos cambios en la clase `TableFormatter` para que utilice el módulo `abc` y se convierta en una clase base abstracta.

1. Primero, necesitamos importar las cosas necesarias del módulo `abc`. Agrega la siguiente declaración de importación en la parte superior del archivo:

```python
# tableformat.py
from abc import ABC, abstractmethod
```

Esta declaración de importación trae dos cosas importantes: `ABC`, que es una clase base para todas las clases base abstractas en Python, y `abstractmethod`, que es un decorador que usaremos para marcar métodos como abstractos.

2. A continuación, modificaremos la clase `TableFormatter`. Debería heredar de `ABC` para convertirse en una clase base abstracta, y marcaremos sus métodos como abstractos utilizando el decorador `@abstractmethod`. Así es como debería verse la clase modificada:

```python
class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        pass

    @abstractmethod
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        pass
```

Observa algunas cosas sobre esta clase modificada:

- La clase ahora hereda de `ABC`, lo que significa que es oficialmente una clase base abstracta.
- Tanto el método `headings` como el método `row` están decorados con `@abstractmethod`. Esto le dice a Python que cualquier subclase de `TableFormatter` debe implementar estos métodos.
- Reemplazamos el `NotImplementedError` con `pass`. El decorador `@abstractmethod` se encarga de asegurarse de que las subclases implementen estos métodos, por lo que ya no necesitamos el `NotImplementedError`.

## Probar tu clase base abstracta

Ahora que hemos convertido la clase `TableFormatter` en una clase base abstracta, probemos si funciona correctamente. Crearemos un archivo llamado `test_abc.py` con el siguiente código:

```python
from tableformat import TableFormatter

# Test case 1: Define a class with a misspelled method
try:
    class NewFormatter(TableFormatter):
        def headers(self, headings):  # Misspelled 'headings'
            pass
        def row(self, rowdata):
            pass

    f = NewFormatter()
    print("Test 1 failed - abstract method enforcement not working")
except TypeError as e:
    print(f"Test 1 passed - caught error: {e}")

# Test case 2: Define a class that properly implements all methods
try:
    class ProperFormatter(TableFormatter):
        def headings(self, headers):
            pass
        def row(self, rowdata):
            pass

    f = ProperFormatter()
    print("Test 2 passed - proper implementation works")
except TypeError as e:
    print(f"Test 2 failed - error: {e}")
```

En este código, tenemos dos casos de prueba. El primer caso de prueba define una clase `NewFormatter` que intenta heredar de `TableFormatter` pero tiene un nombre de método mal escrito. El segundo caso de prueba define una clase `ProperFormatter` que implementa correctamente todos los métodos requeridos.

Para ejecutar la prueba, abre tu terminal y ejecuta el siguiente comando:

```bash
python test_abc.py
```

Deberías ver una salida similar a esta:

```
Test 1 passed - caught error: Can't instantiate abstract class NewFormatter with abstract methods headings
Test 2 passed - proper implementation works
```

Esta salida confirma que nuestra clase base abstracta está funcionando como se esperaba. El primer caso de prueba falla porque la clase `NewFormatter` no implementó correctamente el método `headings`. El segundo caso de prueba pasa porque la clase `ProperFormatter` implementó todos los métodos requeridos.
