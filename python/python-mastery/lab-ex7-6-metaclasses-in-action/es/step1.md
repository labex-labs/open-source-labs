# Comprender el problema

Antes de comenzar a explorar las metaclases, es importante entender el problema que pretendemos resolver. En programación, a menudo necesitamos crear estructuras con tipos específicos para sus atributos. En nuestro trabajo previo, desarrollamos un sistema para estructuras con comprobación de tipos. Este sistema nos permite definir clases donde cada atributo tiene un tipo específico, y los valores asignados a estos atributos se validan de acuerdo con ese tipo.

A continuación, se muestra un ejemplo de cómo usamos este sistema para crear una clase `Stock`:

```python
from validate import String, PositiveInteger, PositiveFloat
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
```

En este código, primero importamos los tipos de validadores (`String`, `PositiveInteger`, `PositiveFloat`) del módulo `validate` y la clase `Structure` del módulo `structure`. Luego definimos la clase `Stock`, que hereda de `Structure`. Dentro de la clase `Stock`, definimos atributos con tipos de validadores específicos. Por ejemplo, el atributo `name` debe ser una cadena, `shares` debe ser un entero positivo y `price` debe ser un número de punto flotante positivo.

Sin embargo, hay un problema con este enfoque. Necesitamos importar todos los tipos de validadores en la parte superior de nuestro archivo. A medida que agregamos más y más tipos de validadores en un escenario del mundo real, estas importaciones pueden volverse muy largas y difíciles de manejar. Esto podría llevarnos a usar `from validate import *`, lo cual generalmente se considera una mala práctica porque puede causar conflictos de nombres y hacer que el código sea menos legible.

Para entender nuestro punto de partida, echemos un vistazo a la clase `Structure`. Debes abrir el archivo `structure.py` en el editor y examinar su contenido. Esto te ayudará a ver cómo se implementa el manejo básico de estructuras antes de agregar la funcionalidad de metaclase.

```bash
code structure.py
```

Cuando abras el archivo, verás una implementación básica de la clase `Structure`. Esta clase es responsable de manejar la inicialización de atributos, pero aún no tiene ninguna funcionalidad de metaclase.

A continuación, examinemos las clases de validadores. Estas clases se definen en el archivo `validate.py`. Ya tienen funcionalidad de descriptor, lo que significa que pueden controlar cómo se accede y se establecen los atributos. Pero necesitaremos mejorarlas para resolver el problema de importación que discutimos anteriormente.

```bash
code validate.py
```

Al observar estas clases de validadores, tendrás una mejor comprensión de cómo funciona el proceso de validación y qué cambios necesitamos hacer para mejorar nuestro código.
