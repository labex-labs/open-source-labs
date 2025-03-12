# Creación de descriptores personalizados

En este paso, vamos a crear nuestra propia clase de descriptor. Pero primero, entendamos qué es un descriptor. Un descriptor es un objeto de Python que implementa el protocolo de descriptores, que consiste en los métodos `__get__`, `__set__` y `__delete__`. Estos métodos permiten al descriptor gestionar cómo se accede, se establece y se elimina un atributo. Al crear nuestra propia clase de descriptor, podemos entender mejor cómo funciona este protocolo.

Crea un nuevo archivo llamado `descrip.py` en el directorio del proyecto. Este archivo contendrá nuestra clase de descriptor personalizado. Aquí está el código:

```python
# descrip.py

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f'{self.name}:__get__')
        # In a real descriptor, you would return a value here

    def __set__(self, instance, value):
        print(f'{self.name}:__set__ {value}')
        # In a real descriptor, you would store the value here

    def __delete__(self, instance):
        print(f'{self.name}:__delete__')
        # In a real descriptor, you would delete the value here
```

En la clase `Descriptor`, el método `__init__` inicializa el descriptor con un nombre. El método `__get__` se llama cuando se accede al atributo, el método `__set__` se llama cuando se establece el atributo y el método `__delete__` se llama cuando se elimina el atributo.

Ahora, creemos un archivo de prueba para experimentar con nuestro descriptor personalizado. Esto nos ayudará a ver cómo se comporta el descriptor en diferentes escenarios. Crea un archivo llamado `test_descrip.py` con el siguiente código:

```python
# test_descrip.py

from descrip import Descriptor

class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

# Create an instance and try accessing the attributes
if __name__ == '__main__':
    f = Foo()
    print("Accessing attribute f.a:")
    f.a

    print("\nAccessing attribute f.b:")
    f.b

    print("\nSetting attribute f.a = 23:")
    f.a = 23

    print("\nDeleting attribute f.a:")
    del f.a
```

En el archivo `test_descrip.py`, importamos la clase `Descriptor` de `descrip.py`. Luego creamos una clase `Foo` con tres atributos `a`, `b` y `c`, cada uno gestionado por un descriptor. Creamos una instancia de `Foo` y realizamos operaciones como acceder, establecer y eliminar atributos para ver cómo se llaman los métodos del descriptor.

Ahora ejecutemos este archivo de prueba para ver los descriptores en acción. Abre tu terminal, navega hasta el directorio del proyecto y ejecuta el archivo de prueba utilizando los siguientes comandos:

```bash
cd ~/project
python3 test_descrip.py
```

Deberías ver una salida como esta:

```
Accessing attribute f.a:
a:__get__

Accessing attribute f.b:
b:__get__

Setting attribute f.a = 23:
a:__set__ 23

Deleting attribute f.a:
a:__delete__
```

Como puedes ver, cada vez que accedes, estableces o eliminas un atributo que está gestionado por un descriptor, se llama al método mágico correspondiente (`__get__`, `__set__` o `__delete__`).

Examinemos también nuestro descriptor de forma interactiva. Esto nos permitirá probar el descriptor en tiempo real y ver los resultados inmediatamente. Abre tu terminal, navega hasta el directorio del proyecto e inicia una sesión interactiva de Python con el archivo `descrip.py`:

```bash
cd ~/project
python3 -i descrip.py
```

Ahora escribe estos comandos en la sesión interactiva de Python para ver cómo funciona el protocolo de descriptores:

```python
class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

f = Foo()
f.a         # Should call __get__
f.b         # Should call __get__
f.a = 23    # Should call __set__
del f.a     # Should call __delete__
exit()
```

La idea clave aquí es que los descriptores proporcionan una forma de interceptar y personalizar el acceso a los atributos. Esto los hace poderosos para implementar validación de datos, atributos calculados y otros comportamientos avanzados. Al usar descriptores, puedes tener más control sobre cómo se accede, se establece y se elimina los atributos de tu clase.
