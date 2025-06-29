# Delegación como alternativa a la herencia

En la programación orientada a objetos, reutilizar y extender código es una tarea común. Hay dos formas principales de lograr esto: la herencia y la delegación.

**La herencia** es un mecanismo en el que una subclase hereda métodos y atributos de una clase padre. La subclase puede elegir anular algunos de estos métodos heredados para proporcionar su propia implementación.

**La delegación**, por otro lado, implica que un objeto contenga otro objeto y reenvíe llamadas a métodos específicos a él.

En este paso, exploraremos la delegación como alternativa a la herencia. Implementaremos una clase que delegue parte de su comportamiento a otro objeto.

## Configuración de un ejemplo de delegación

Primero, necesitamos configurar la clase base con la que interactuará nuestra clase delegadora.

1. Crea un nuevo archivo llamado `base_class.py` en el directorio `/home/labex/project`. Este archivo definirá una clase llamada `Spam` con tres métodos: `method_a`, `method_b` y `method_c`. Cada método imprime un mensaje y devuelve un resultado. Aquí está el código que debes poner en `base_class.py`:

```python
class Spam:
    def method_a(self):
        print('Spam.method_a executed')
        return "Result from Spam.method_a"

    def method_b(self):
        print('Spam.method_b executed')
        return "Result from Spam.method_b"

    def method_c(self):
        print('Spam.method_c executed')
        return "Result from Spam.method_c"
```

A continuación, crearemos la clase delegadora.

2. Crea un nuevo archivo llamado `delegator.py`. En este archivo, definiremos una clase llamada `DelegatingSpam` que delegue parte de su comportamiento a una instancia de la clase `Spam`.

```python
from base_class import Spam

class DelegatingSpam:
    def __init__(self):
        # Create an instance of Spam that we'll delegate to
        self._spam = Spam()

    def method_a(self):
        # Override method_a but also call the original
        print('DelegatingSpam.method_a executed')
        result = self._spam.method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('DelegatingSpam.method_c executed')
        return "Result from DelegatingSpam.method_c"

    def __getattr__(self, name):
        # For any other attribute/method, delegate to self._spam
        print(f"Delegating {name} to the wrapped Spam object")
        return getattr(self._spam, name)
```

En el método `__init__`, creamos una instancia de la clase `Spam`. El método `method_a` anula el método original pero también llama al `method_a` de la clase `Spam`. El método `method_c` anula completamente el método original. El método `__getattr__` es un método especial en Python que se llama cuando se accede a un atributo o método que no existe en la clase `DelegatingSpam`. Luego delega la llamada a la instancia de `Spam`.

Ahora, creemos un archivo de prueba para verificar nuestra implementación.

3. Crea un archivo de prueba llamado `test_delegation.py`. Este archivo creará una instancia de la clase `DelegatingSpam` y llamará a sus métodos.

```python
from delegator import DelegatingSpam

# Create a delegating object
spam = DelegatingSpam()

print("Calling method_a (overridden with delegation):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (not defined in DelegatingSpam, delegated):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Finalmente, ejecutaremos el script de prueba.

4. Ejecuta el script de prueba usando los siguientes comandos en la terminal:

```bash
cd /home/labex/project
python3 test_delegation.py
```

Deberías ver una salida similar a la siguiente:

```
Calling method_a (overridden with delegation):
DelegatingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (not defined in DelegatingSpam, delegated):
Delegating method_b to the wrapped Spam object
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
DelegatingSpam.method_c executed
Result: Result from DelegatingSpam.method_c

Calling non-existent method_d:
Delegating method_d to the wrapped Spam object
Error: 'Spam' object has no attribute 'method_d'
```

## Delegación vs. Herencia

Ahora, comparemos la delegación con la herencia tradicional.

1. Crea un archivo llamado `inheritance_example.py`. En este archivo, definiremos una clase llamada `InheritingSpam` que herede de la clase `Spam`.

```python
from base_class import Spam

class InheritingSpam(Spam):
    def method_a(self):
        # Override method_a but also call the parent method
        print('InheritingSpam.method_a executed')
        result = super().method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('InheritingSpam.method_c executed')
        return "Result from InheritingSpam.method_c"
```

La clase `InheritingSpam` anula los métodos `method_a` y `method_c`. En el método `method_a`, usamos `super()` para llamar al `method_a` de la clase padre.

A continuación, crearemos un archivo de prueba para el ejemplo de herencia.

2. Crea un archivo de prueba llamado `test_inheritance.py`. Este archivo creará una instancia de la clase `InheritingSpam` y llamará a sus métodos.

```python
from inheritance_example import InheritingSpam

# Create an inheriting object
spam = InheritingSpam()

print("Calling method_a (overridden with super call):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (inherited from parent):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Finalmente, ejecutaremos la prueba de herencia.

3. Ejecuta la prueba de herencia usando los siguientes comandos en la terminal:

```bash
cd /home/labex/project
python3 test_inheritance.py
```

Deberías ver una salida similar a la siguiente:

```
Calling method_a (overridden with super call):
InheritingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (inherited from parent):
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
InheritingSpam.method_c executed
Result: Result from InheritingSpam.method_c

Calling non-existent method_d:
Error: 'InheritingSpam' object has no attribute 'method_d'
```

## Diferencias clave y consideraciones

Veamos las similitudes y diferencias entre la delegación y la herencia.

1. **Anulación de métodos**: Tanto la delegación como la herencia te permiten anular métodos, pero la sintaxis es diferente.
   - En la delegación, defines tu propio método y decides si llamar al método del objeto envuelto.
   - En la herencia, defines tu propio método y usas `super()` para llamar al método de la clase padre.

2. **Acceso a métodos**:
   - En la delegación, los métodos no definidos se reenvían a través del método `__getattr__`.
   - En la herencia, los métodos no definidos se heredan automáticamente.

3. **Relaciones de tipo**:
   - Con la delegación, `isinstance(delegating_spam, Spam)` devuelve `False` porque el objeto `DelegatingSpam` no es una instancia de la clase `Spam`.
   - Con la herencia, `isinstance(inheriting_spam, Spam)` devuelve `True` porque la clase `InheritingSpam` hereda de la clase `Spam`.

4. **Limitaciones**: La delegación a través de `__getattr__` no funciona con métodos especiales como `__getitem__`, `__len__`, etc. Estos métodos deben definirse explícitamente en la clase delegadora.

La delegación es especialmente útil en las siguientes situaciones:

- Quieres personalizar el comportamiento de un objeto sin afectar su jerarquía.
- Quieres combinar comportamientos de múltiples objetos que no comparten un padre común.
- Necesitas más flexibilidad de la que proporciona la herencia.

La herencia se prefiere generalmente cuando:

- La relación "es-un" es clara (por ejemplo, un automóvil es un vehículo).
- Necesitas mantener la compatibilidad de tipos en tu código.
- Los métodos especiales deben heredarse.
