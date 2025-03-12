# Manejo de excepciones en generadores

En este paso, aprenderemos cómo manejar excepciones en generadores y corutinas. Pero primero, entendamos qué son las excepciones. Una excepción es un evento que ocurre durante la ejecución de un programa y altera el flujo normal de las instrucciones del programa. En Python, podemos usar el método `throw()` para manejar excepciones en generadores y corutinas.

## Comprender las corutinas

Una corutina es un tipo especial de generador. A diferencia de los generadores regulares que principalmente producen valores, las corutinas pueden tanto consumir valores (usando el método `send()`) como producir valores. El archivo `cofollow.py` tiene una implementación sencilla de una corutina.

Abriremos el archivo `cofollow.py` en el editor WebIDE. Aquí está el código dentro:

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def printer():
    while True:
        item = yield
        print(item)
```

Ahora, desglosemos este código. El `consumer` es un decorador. Un decorador es una función que toma otra función como argumento, le agrega alguna funcionalidad y luego devuelve la función modificada. En este caso, el decorador `consumer` mueve automáticamente el generador a su primera declaración `yield`. Esto es importante porque hace que el generador esté listo para recibir valores.

La corutina `printer()` se define con el decorador `@consumer`. Dentro de la función `printer()`, tenemos un bucle `while` infinito. La declaración `item = yield` es donde ocurre la magia. Pausa la ejecución de la corutina y espera a recibir un valor. Cuando se envía un valor a la corutina, se reanuda la ejecución y se imprime el valor recibido.

## Agregar manejo de excepciones a la corutina

Ahora, modificaremos la corutina `printer()` para manejar excepciones. Actualizaremos la función `printer()` en `cofollow.py` de la siguiente manera:

```python
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

El bloque `try` contiene el código que podría generar una excepción. En nuestro caso, es el código que recibe e imprime el valor. Si ocurre una excepción en el bloque `try`, la ejecución salta al bloque `except`. El bloque `except` captura la excepción e imprime un mensaje de error. Después de realizar estos cambios, guarda el archivo.

## Experimentar con el manejo de excepciones en corutinas

Comencemos a experimentar lanzando excepciones a la corutina. Abre una terminal y ejecuta el intérprete de Python usando los siguientes comandos:

```bash
cd ~/project
python3
```

### Experimento 1: Uso básico de la corutina

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')  # Send a value to the coroutine
hello
>>> p.send(42)  # Send another value
42
```

Aquí, primero importamos la corutina `printer` del módulo `cofollow`. Luego creamos una instancia de la corutina `printer` llamada `p`. Usamos el método `send()` para enviar valores a la corutina. Como se puede ver, la corutina procesa los valores que le enviamos sin problemas.

### Experimento 2: Lanzar una excepción a la corutina

```python
>>> p.throw(ValueError('It failed'))  # Throw an exception into the coroutine
ERROR: ValueError('It failed')
```

En este experimento, usamos el método `throw()` para inyectar una excepción `ValueError` en la corutina. El bloque `try-except` en la corutina `printer()` captura la excepción e imprime un mensaje de error. Esto muestra que nuestro manejo de excepciones funciona como se espera.

### Experimento 3: Lanzar una excepción real a la corutina

```python
>>> try:
...     int('n/a')  # This will raise a ValueError
... except ValueError as e:
...     p.throw(e)  # Throw the caught exception into the coroutine
...
ERROR: ValueError("invalid literal for int() with base 10: 'n/a'")
```

Aquí, primero intentamos convertir la cadena `'n/a'` a un entero, lo que genera una excepción `ValueError`. Capturamos esta excepción y luego usamos el método `throw()` para pasarla a la corutina. La corutina captura la excepción e imprime el mensaje de error.

### Experimento 4: Verificar que la corutina sigue funcionando

```python
>>> p.send('still working')  # The coroutine continues to run after handling exceptions
still working
```

Después de manejar las excepciones, enviamos otro valor a la corutina usando el método `send()`. La corutina sigue activa y puede procesar el nuevo valor. Esto muestra que nuestra corutina puede seguir funcionando incluso después de encontrar errores.

## Puntos clave

1. Los generadores y las corutinas pueden manejar excepciones en el punto de la declaración `yield`. Esto significa que podemos capturar y manejar errores que ocurren cuando la corutina está esperando o procesando un valor.
2. El método `throw()` te permite inyectar excepciones en un generador o corutina. Esto es útil para pruebas y para manejar errores que ocurren fuera de la corutina.
3. Manejar adecuadamente las excepciones en generadores te permite crear generadores robustos y tolerantes a errores que pueden seguir funcionando incluso cuando se producen errores. Esto hace que tu código sea más confiable y fácil de mantener.

Para salir del intérprete de Python, puedes escribir `exit()` o presionar `Ctrl+D`.
