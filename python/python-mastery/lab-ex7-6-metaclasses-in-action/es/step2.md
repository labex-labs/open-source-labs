# Recopilación de tipos de validadores

En Python, los validadores son clases que nos ayudan a garantizar que los datos cumplan con ciertos criterios. Nuestra primera tarea en este experimento es modificar la clase base `Validator` para que pueda recopilar todas sus subclases. ¿Por qué necesitamos hacer esto? Bueno, al recopilar todas las subclases de validadores, podemos crear un espacio de nombres que contenga todos los tipos de validadores. Más adelante, inyectaremos este espacio de nombres en la clase `Structure`, lo que nos permitirá manejar y utilizar diferentes validadores de manera más sencilla.

Ahora, comencemos a trabajar en el código. Abre el archivo `validate.py`. Puedes usar el siguiente comando en la terminal para abrirlo:

```bash
code validate.py
```

Una vez abierto el archivo, necesitamos agregar un diccionario a nivel de clase y un método `__init_subclass__()` a la clase `Validator`. El diccionario a nivel de clase se utilizará para almacenar todas las subclases de validadores, y el método `__init_subclass__()` es un método especial en Python que se llama cada vez que se define una subclase de la clase actual.

Agrega el siguiente código a la clase `Validator`, justo después de la definición de la clase:

```python
# Add this to the Validator class in validate.py
validators = {}  # Dictionary to collect all validator subclasses

@classmethod
def __init_subclass__(cls):
    """Register each validator subclass in the validators dictionary"""
    Validator.validators[cls.__name__] = cls
```

Después de agregar el código, tu clase `Validator` modificada debería verse así:

```python
class Validator:
    validators = {}  # Dictionary to collect all validator subclasses

    @classmethod
    def __init_subclass__(cls):
        """Register each validator subclass in the validators dictionary"""
        Validator.validators[cls.__name__] = cls

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value):
        pass
```

Ahora, cada vez que se defina un nuevo tipo de validador, como `String` o `PositiveInteger`, Python llamará automáticamente al método `__init_subclass__()`. Este método agregará la nueva subclase de validador al diccionario `validators`, utilizando el nombre de la clase como clave.

Probemos si nuestro código funciona. Crearemos un script de Python simple para verificar el contenido del diccionario `validators`. Puedes ejecutar el siguiente comando en la terminal:

```bash
python3 -c "from validate import Validator; print(Validator.validators)"
```

Si todo funciona correctamente, deberías ver una salida similar a esta, que muestra todos los tipos de validadores y sus clases correspondientes:

```
{'Typed': <class 'validate.Typed'>, 'Positive': <class 'validate.Positive'>, 'NonEmpty': <class 'validate.NonEmpty'>, 'String': <class 'validate.String'>, 'Integer': <class 'validate.Integer'>, 'Float': <class 'validate.Float'>, 'PositiveInteger': <class 'validate.PositiveInteger'>, 'PositiveFloat': <class 'validate.PositiveFloat'>, 'NonEmptyString': <class 'validate.NonEmptyString'>}
```

Ahora que tenemos un diccionario que contiene todos nuestros tipos de validadores, podemos usarlo en el siguiente paso para crear nuestra metaclase.
