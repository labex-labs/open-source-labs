# Creando tu Primera Metaclase

Ahora, vamos a crear nuestra primera metaclase. Antes de comenzar a codificar, entendamos qué es una metaclase. En Python, una metaclase es una clase que crea otras clases. Es como un plano para las clases. Cuando defines una clase en Python, Python utiliza una metaclase para crear esa clase. Por defecto, Python utiliza la metaclase `type`. En este paso, definiremos una metaclase personalizada que imprima información sobre la clase que está creando. Esto nos ayudará a entender cómo funcionan las metaclases por debajo.

1. Abre VSCode en el WebIDE y crea un nuevo archivo llamado `mymeta.py` en el directorio `/home/labex/project`. Aquí es donde escribiremos nuestro código para la metaclase.

2. Agrega el siguiente código al archivo:

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

Desglosemos lo que hace este código:

- Primero, definimos una nueva clase llamada `mytype` que hereda de `type`. Dado que `type` es la metaclase predeterminada en Python, al heredar de ella, estamos creando nuestra propia metaclase personalizada.
- A continuación, sobrescribimos el método `__new__`. En Python, el método `__new__` es un método especial que se llama cuando se crea un nuevo objeto. En el contexto de una metaclase, se llama cuando se crea una nueva clase.
- Dentro de nuestro método `__new__`, imprimimos alguna información sobre la clase que se está creando. Imprimimos el nombre de la clase, sus clases base y sus atributos. Después de eso, llamamos al método `__new__` del padre utilizando `super().__new__(meta, name, bases, __dict__)`. Esto es importante porque en realidad crea la clase.
- Finalmente, creamos una clase base llamada `myobject` y especificamos que debe utilizar nuestra metaclase personalizada `mytype`.

El método `__new__` toma los siguientes parámetros:

- `meta`: Esto se refiere a la metaclase en sí. En nuestro caso, es `mytype`.
- `name`: Este es el nombre de la clase que se está creando.
- `bases`: Esta es una tupla que contiene las clases base de las que hereda la nueva clase.
- `__dict__`: Este es un diccionario que contiene los atributos de la clase.

3. Guarda el archivo presionando Ctrl+S o haciendo clic en Archivo > Guardar. Guardar el archivo asegura que tu código se conserve y se pueda ejecutar más tarde.
