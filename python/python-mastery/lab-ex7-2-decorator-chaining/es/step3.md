# Aplicación de decoradores a métodos de clase

Ahora, vamos a explorar cómo los decoradores interactúan con los métodos de clase. Esto puede ser un poco complicado porque Python tiene diferentes tipos de métodos: métodos de instancia, métodos de clase, métodos estáticos y propiedades. Los decoradores son funciones que toman otra función y extienden el comportamiento de esta última sin modificarla explícitamente. Cuando se aplican decoradores a métodos de clase, debemos prestar atención a cómo funcionan con estos diferentes tipos de métodos.

## Comprendiendo el desafío

Veamos qué sucede cuando aplicamos nuestro decorador `@logged` a diferentes tipos de métodos. El decorador `@logged` probablemente se utiliza para registrar información sobre las llamadas a los métodos.

1. Crea un nuevo archivo `methods.py` en el WebIDE. Este archivo contendrá nuestra clase con diferentes tipos de métodos decorados con el decorador `@logged`.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @logged
    @classmethod
    def class_method(cls):
        print("Class method called")
        return "class result"

    @logged
    @staticmethod
    def static_method():
        print("Static method called")
        return "static result"

    @logged
    @property
    def property_method(self):
        print("Property method called")
        return "property result"
```

En este código, tenemos una clase `Spam` con cuatro tipos diferentes de métodos. Cada método está decorado con el decorador `@logged`, y algunos también están decorados con otros decoradores incorporados como `@classmethod`, `@staticmethod` y `@property`.

2. Probemos cómo funciona. Ejecutaremos un comando de Python en la terminal para llamar a estos métodos y ver la salida.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

Cuando ejecutes este comando, es posible que notes algunos problemas:

- El decorador `@property` puede no funcionar correctamente con nuestro decorador `@logged`. El decorador `@property` se utiliza para definir un método como una propiedad, y tiene una forma específica de funcionar. Cuando se combina con el decorador `@logged`, pueden haber conflictos.
- El orden de los decoradores es importante para `@classmethod` y `@staticmethod`. El orden en el que se aplican los decoradores puede cambiar el comportamiento del método.

## El orden de los decoradores

Cuando se aplican múltiples decoradores, se aplican de abajo hacia arriba. Esto significa que el decorador más cercano a la definición del método se aplica primero, y luego los que están por encima se aplican en secuencia. Por ejemplo:

```python
@decorator1
@decorator2
def func():
    pass
```

Esto es equivalente a:

```python
func = decorator1(decorator2(func))
```

En este ejemplo, `decorator2` se aplica a `func` primero, y luego `decorator1` se aplica al resultado de `decorator2(func)`.

## Corrigiendo el orden de los decoradores

Vamos a actualizar nuestro archivo `methods.py` para corregir el orden de los decoradores. Al cambiar el orden de los decoradores, podemos asegurarnos de que cada método funcione como se espera.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @classmethod
    @logged
    def class_method(cls):
        print("Class method called")
        return "class result"

    @staticmethod
    @logged
    def static_method():
        print("Static method called")
        return "static result"

    @property
    @logged
    def property_method(self):
        print("Property method called")
        return "property result"
```

En esta versión actualizada:

- Para `instance_method`, el orden no importa. Los métodos de instancia se llaman en una instancia de la clase, y el decorador `@logged` se puede aplicar en cualquier orden sin afectar su funcionalidad básica.
- Para `class_method`, aplicamos `@classmethod` después de `@logged`. El decorador `@classmethod` cambia la forma en que se llama al método, y aplicarlo después de `@logged` asegura que el registro funcione correctamente.
- Para `static_method`, aplicamos `@staticmethod` después de `@logged`. Similar al `@classmethod`, el decorador `@staticmethod` tiene su propio comportamiento, y el orden con el decorador `@logged` debe ser correcto.
- Para `property_method`, aplicamos `@property` después de `@logged`. Esto asegura que se mantenga el comportamiento de la propiedad mientras también se obtiene la funcionalidad de registro.

3. Probemos el código actualizado. Ejecutaremos el mismo comando que antes para ver si se solucionan los problemas.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

Ahora deberías ver un registro adecuado para todos los tipos de métodos:

```
Calling instance_method
Instance method called
instance result
Calling class_method
Class method called
class result
Calling static_method
Static method called
static result
Calling property_method
Property method called
property result
```

## Mejores prácticas para decoradores de métodos

Cuando trabajes con decoradores de métodos, sigue estas mejores prácticas:

1. Aplica los decoradores que transforman métodos (`@classmethod`, `@staticmethod`, `@property`) **después** de tus decoradores personalizados. Esto asegura que los decoradores personalizados puedan realizar su registro u otras operaciones primero, y luego los decoradores incorporados puedan transformar el método como se pretendía.
2. Ten en cuenta que la ejecución del decorador se produce en el momento de la definición de la clase, no en el momento de la llamada al método. Esto significa que cualquier código de configuración o inicialización en el decorador se ejecutará cuando se defina la clase, no cuando se llame al método.
3. Para casos más complejos, es posible que debas crear decoradores especializados para diferentes tipos de métodos. Diferentes tipos de métodos tienen diferentes comportamientos, y un decorador único no puede funcionar en todas las situaciones.
