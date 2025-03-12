# Creando tu primer decorador

## ¿Qué son los decoradores?

En Python, los decoradores son una sintaxis especial que puede ser muy útil para los principiantes. Permiten modificar el comportamiento de funciones o métodos. Puedes pensar en un decorador como una función que toma otra función como entrada y luego devuelve una nueva función. Esta nueva función a menudo extiende o cambia el comportamiento de la función original.

Los decoradores se aplican utilizando el símbolo `@`. Colocas este símbolo seguido del nombre del decorador directamente encima de la definición de una función. Esta es una forma sencilla de decirle a Python que quieres usar el decorador en esa función en particular.

## Creando un decorador de registro (logging) simple

Vamos a crear un decorador simple que registre información cuando se llama a una función. El registro es una tarea común en aplicaciones del mundo real, y usar un decorador para esto es una excelente manera de entender cómo funcionan.

1. Primero, abre el editor VSCode. En el directorio `/home/labex/project`, crea un nuevo archivo llamado `logcall.py`. Este archivo contendrá nuestra función decorador.

2. Agrega el siguiente código a `logcall.py`:

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Analicemos lo que hace este código:

- La función `logged` es nuestro decorador. Toma otra función, que llamamos `func`, como argumento. Esta `func` es la función a la que queremos agregar registro.
- Cuando se aplica el decorador a una función, imprime un mensaje. Este mensaje nos dice que se está agregando registro a la función con el nombre dado.
- Dentro de la función `logged`, definimos una función interna llamada `wrapper`. Esta función `wrapper` es la que reemplazará a la función original.
  - Cuando se llama a la función decorada, la función `wrapper` imprime un mensaje que dice que se está llamando a la función.
  - Luego llama a la función original (`func`) con todos los argumentos que se le pasaron. Los `*args` y `**kwargs` se utilizan para aceptar cualquier número de argumentos posicionales y de palabra clave.
  - Finalmente, devuelve el resultado de la función original.
- La función `logged` devuelve la función `wrapper`. Esta función `wrapper` se utilizará ahora en lugar de la función original, agregando la funcionalidad de registro.

## Usando el decorador

3. Ahora, en el mismo directorio (`/home/labex/project`), crea otro archivo llamado `sample.py` con el siguiente código:

```python
# sample.py

from logcall import logged

@logged
def add(x, y):
    return x + y

@logged
def sub(x, y):
    return x - y
```

La sintaxis `@logged` es muy importante aquí. Le dice a Python que aplique el decorador `logged` a las funciones `add` y `sub`. Entonces, cada vez que se llamen estas funciones, se ejecutará la funcionalidad de registro agregada por el decorador.

## Probando el decorador

4. Para probar tu decorador, abre una terminal en VSCode. Primero, cambia el directorio al directorio del proyecto usando el siguiente comando:

```bash
cd /home/labex/project
```

Luego, inicia el intérprete de Python:

```bash
python3
```

5. En el intérprete de Python, importa el módulo `sample` y prueba las funciones decoradas:

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3, 4)
Calling add
7
>>> sample.sub(2, 3)
Calling sub
-1
>>> exit()
```

Observa que cuando importas el módulo `sample`, se imprimen los mensajes "Adding logging to...". Esto se debe a que el decorador se aplica cuando se importa el módulo. Cada vez que llamas a una de las funciones decoradas, se imprime el mensaje "Calling...". Esto muestra que el decorador está funcionando como se esperaba.

Este decorador simple demuestra el concepto básico de los decoradores. Envuelve la función original con funcionalidad adicional (registro en este caso) sin cambiar el código de la función original. Esta es una característica poderosa en Python que puedes usar en muchos escenarios diferentes.
