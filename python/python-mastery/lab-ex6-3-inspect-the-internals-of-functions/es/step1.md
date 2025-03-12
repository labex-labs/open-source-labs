# Explorando los atributos de las funciones

En Python, las funciones se consideran objetos de primera clase. ¿Qué significa esto? Bueno, es similar a cómo en el mundo real hay diferentes tipos de objetos, como un libro o un bolígrafo. En Python, las funciones también son objetos y, al igual que otros objetos, tienen su propio conjunto de atributos. Estos atributos pueden darnos mucha información útil sobre la función, como su nombre, dónde está definida y cómo está implementada.

Comencemos nuestra exploración abriendo una shell interactiva de Python. Esta shell es como un campo de juego donde podemos escribir y ejecutar código de Python de inmediato. Para hacer esto, primero navegaremos al directorio del proyecto y luego iniciaremos el intérprete de Python. Aquí están los comandos para ejecutar en tu terminal:

```bash
cd ~/project
python3
```

Ahora que estamos en la shell interactiva de Python, definamos una función simple. Esta función tomará dos números y los sumará. Así es como podemos definirla:

```python
def add(x, y):
    'Adds two things'
    return x + y
```

En este código, hemos creado una función llamada `add`. Toma dos parámetros, `x` y `y`, y devuelve su suma. La cadena `'Adds two things'` se llama docstring, que se utiliza para documentar lo que hace la función.

## Usando `dir()` para inspeccionar los atributos de una función

En Python, la función `dir()` es una herramienta muy útil. Se puede utilizar para obtener una lista de todos los atributos y métodos que tiene un objeto. Usémosla para ver qué atributos tiene nuestra función `add`. Ejecuta el siguiente código en la shell interactiva de Python:

```python
dir(add)
```

Cuando ejecutes este código, verás una larga lista de atributos. Aquí tienes un ejemplo de cómo podría verse la salida:

```
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

Esta lista muestra todos los atributos y métodos asociados con la función `add`.

## Accediendo a la información básica de una función

Ahora, echemos un vistazo más de cerca a algunos de los atributos básicos de una función. Estos atributos pueden darnos información importante sobre la función. Ejecuta el siguiente código en la shell interactiva de Python:

```python
print(add.__name__)
print(add.__module__)
print(add.__doc__)
```

Cuando ejecutes este código, verás la siguiente salida:

```
add
__main__
Adds two things
```

Entendamos lo que significa cada uno de estos atributos:

- `__name__`: Este atributo nos da el nombre de la función. En nuestro caso, la función se llama `add`.
- `__module__`: Nos dice el módulo donde está definida la función. Cuando ejecutamos código en la shell interactiva, el módulo suele ser `__main__`.
- `__doc__`: Esta es la cadena de documentación de la función, o docstring. Proporciona una breve descripción de lo que hace la función.

## Examinando el código de una función

El atributo `__code__` de una función es muy interesante. Contiene información sobre cómo está implementada la función, incluyendo su bytecode y otros detalles. Veamos qué podemos aprender de él. Ejecuta el siguiente código en la shell interactiva de Python:

```python
print(add.__code__.co_varnames)
print(add.__code__.co_argcount)
```

La salida será:

```
('x', 'y')
2
```

Esto es lo que nos dicen estos atributos:

- `co_varnames`: Es una tupla que contiene los nombres de todas las variables locales utilizadas por la función. En nuestra función `add`, las variables locales son `x` y `y`.
- `co_argcount`: Este atributo nos dice el número de argumentos que espera la función. Nuestra función `add` espera dos argumentos, por lo que el valor es 2.

Si estás curioso por explorar más atributos del objeto `__code__`, puedes usar la función `dir()` de nuevo. Ejecuta el siguiente código:

```python
dir(add.__code__)
```

Esto mostrará todos los atributos del objeto de código, que contienen detalles de bajo nivel sobre cómo está implementada la función.
