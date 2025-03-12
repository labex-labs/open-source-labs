# Comprender el paso de argumentos de funciones

En Python, las funciones son un concepto fundamental que te permite agrupar un conjunto de instrucciones para realizar una tarea específica. Cuando llamas a una función, a menudo necesitas proporcionarle algunos datos, que llamamos argumentos. Python ofrece diferentes formas de pasar estos argumentos a las funciones. Esta flexibilidad es increíblemente útil, ya que te ayuda a escribir un código más limpio y mantenible. Antes de comenzar a aplicar estas técnicas a nuestro proyecto, echemos un vistazo más detallado a estas convenciones de paso de argumentos.

## Crear una copia de seguridad de tu trabajo

Antes de comenzar a hacer cambios en nuestro archivo `stock.py`, es una buena práctica crear una copia de seguridad. De esta manera, si algo sale mal durante nuestras pruebas, siempre podemos volver a la versión original. Para crear una copia de seguridad, abre una terminal y ejecuta el siguiente comando:

```bash
cp stock.py orig_stock.py
```

Este comando utiliza el comando `cp` (copiar) en la terminal. Toma el archivo `stock.py` y crea una copia de él llamada `orig_stock.py`. Al hacer esto, nos aseguramos de que nuestro trabajo original se conserve de manera segura.

## Explorar el paso de argumentos de funciones

En Python, hay varias formas de llamar a funciones con diferentes tipos de argumentos. Exploremos cada uno de estos métodos en detalle.

### 1. Argumentos posicionales

La forma más sencilla de pasar argumentos a una función es por posición. Cuando defines una función, especificas una lista de parámetros. Cuando llamas a la función, proporcionas valores para estos parámetros en el mismo orden en que se definen.

Aquí tienes un ejemplo:

```python
def calculate(x, y, z):
    return x + y + z

# Call with positional arguments
result = calculate(1, 2, 3)
print(result)  # Output: 6
```

En este ejemplo, la función `calculate` toma tres parámetros: `x`, `y` y `z`. Cuando llamamos a la función con `calculate(1, 2, 3)`, el valor `1` se asigna a `x`, `2` se asigna a `y` y `3` se asigna a `z`. La función luego suma estos valores y devuelve el resultado.

### 2. Argumentos de palabra clave

Además de los argumentos posicionales, también puedes especificar argumentos por sus nombres. Esto se llama usar argumentos de palabra clave. Cuando usas argumentos de palabra clave, no tienes que preocuparte por el orden de los argumentos.

Aquí tienes un ejemplo:

```python
# Call with a mix of positional and keyword arguments
result = calculate(1, z=3, y=2)
print(result)  # Output: 6
```

En este ejemplo, primero pasamos el argumento posicional `1` para `x`. Luego, usamos argumentos de palabra clave para especificar los valores de `y` y `z`. El orden de los argumentos de palabra clave no importa, siempre y cuando proporciones los nombres correctos.

### 3. Desempaquetar secuencias y diccionarios

Python proporciona una forma conveniente de pasar secuencias y diccionarios como argumentos utilizando la sintaxis `*` y `**`. Esto se llama desempaquetado.

Aquí tienes un ejemplo de desempaquetar una tupla en argumentos posicionales:

```python
# Unpacking a tuple into positional arguments
args = (1, 2, 3)
result = calculate(*args)
print(result)  # Output: 6
```

En este ejemplo, tenemos una tupla `args` que contiene los valores `1`, `2` y `3`. Cuando usamos el operador `*` antes de `args` en la llamada a la función, Python desempaqueta la tupla y pasa sus elementos como argumentos posicionales a la función `calculate`.

Aquí tienes un ejemplo de desempaquetar un diccionario en argumentos de palabra clave:

```python
# Unpacking a dictionary into keyword arguments
kwargs = {'y': 2, 'z': 3}
result = calculate(1, **kwargs)
print(result)  # Output: 6
```

En este ejemplo, tenemos un diccionario `kwargs` que contiene los pares clave-valor `'y': 2` y `'z': 3`. Cuando usamos el operador `**` antes de `kwargs` en la llamada a la función, Python desempaqueta el diccionario y pasa sus pares clave-valor como argumentos de palabra clave a la función `calculate`.

### 4. Aceptar argumentos variables

A veces, es posible que desees definir una función que pueda aceptar cualquier número de argumentos. Python te permite hacer esto utilizando la sintaxis `*` y `**` en la definición de la función.

Aquí tienes un ejemplo de una función que acepta cualquier número de argumentos posicionales:

```python
# Accept any number of positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2))           # Output: 3
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
```

En este ejemplo, la función `sum_all` utiliza el parámetro `*args` para aceptar cualquier número de argumentos posicionales. El operador `*` recoge todos los argumentos posicionales en una tupla llamada `args`. La función luego utiliza la función incorporada `sum` para sumar todos los elementos de la tupla.

Aquí tienes un ejemplo de una función que acepta cualquier número de argumentos de palabra clave:

```python
# Accept any number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Python", year=1991)
# Output:
# name: Python
# year: 1991
```

En este ejemplo, la función `print_info` utiliza el parámetro `**kwargs` para aceptar cualquier número de argumentos de palabra clave. El operador `**` recoge todos los argumentos de palabra clave en un diccionario llamado `kwargs`. La función luego itera sobre los pares clave-valor en el diccionario y los imprime.

Estas técnicas nos ayudarán a crear estructuras de código más flexibles y reutilizables en los siguientes pasos. Para familiarizarte más con estos conceptos, abramos el intérprete de Python y probemos algunos de estos ejemplos.

```bash
python3
```

Una vez que estés en el intérprete de Python, intenta ingresar los ejemplos anteriores. Esto te dará experiencia práctica con estas técnicas de paso de argumentos.
