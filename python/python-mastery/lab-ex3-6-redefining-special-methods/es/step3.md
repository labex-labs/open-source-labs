# Creando un gestor de contexto (context manager)

Un gestor de contexto es un tipo especial de objeto en Python. En Python, los objetos pueden tener diferentes métodos que definen su comportamiento. Un gestor de contexto define específicamente dos métodos importantes: `__enter__` y `__exit__`. Estos métodos trabajan en conjunto con la declaración `with`. La declaración `with` se utiliza para establecer un contexto específico para un bloque de código. Piénsalo como crear un pequeño entorno donde ocurren ciertas cosas, y cuando el bloque de código termina, el gestor de contexto se encarga de la limpieza.

En este paso, vamos a crear un gestor de contexto que tiene una función muy útil. Redirigirá temporalmente la salida estándar (`sys.stdout`). La salida estándar es donde va la salida normal de tu programa de Python, generalmente la consola. Al redirigirla, podemos enviar la salida a un archivo en lugar de la consola. Esto es útil cuando quieres guardar la salida que de otro modo solo se mostraría en la consola.

Primero, necesitamos crear un nuevo archivo para escribir el código de nuestro gestor de contexto. Llamaremos a este archivo `redirect.py`. Puedes crearlo utilizando el siguiente comando en la terminal:

```bash
touch /home/labex/project/redirect.py
```

Ahora que el archivo está creado, ábrelo en un editor. Una vez abierto, agrega el siguiente código de Python al archivo:

```python
import sys

class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout
```

Analicemos lo que hace este gestor de contexto:

1. `__init__`: Este es el método de inicialización. Cuando creamos una instancia de la clase `redirect_stdout`, pasamos un objeto de archivo. Este método almacena ese objeto de archivo en la variable de instancia `self.out_file`. Así, recuerda a dónde queremos redirigir la salida.
2. `__enter__`:
   - Primero, guarda el `sys.stdout` actual. Esto es importante porque necesitamos restaurarlo más tarde.
   - Luego, reemplaza el `sys.stdout` actual con nuestro objeto de archivo. A partir de este momento, cualquier salida que normalmente iría a la consola irá al archivo en su lugar.
   - Finalmente, devuelve el objeto de archivo. Esto es útil porque es posible que queramos usar el objeto de archivo dentro del bloque `with`.
3. `__exit__`:
   - Este método restaura el `sys.stdout` original. Así, después de que el bloque `with` termine, la salida volverá a la consola como de costumbre.
   - Toma tres parámetros: tipo de excepción (`ty`), valor de excepción (`val`) y traza de pila (`tb`). Estos parámetros son requeridos por el protocolo de gestores de contexto. Se utilizan para manejar cualquier excepción que pueda ocurrir dentro del bloque `with`.

Ahora, probemos nuestro gestor de contexto. Lo usaremos para redirigir la salida de una tabla a un archivo. Primero, inicia el intérprete de Python:

```bash
python3
```

Luego, ejecuta el siguiente código de Python en el intérprete:

```python
>>> import stock, reader, tableformat
>>> from redirect import redirect_stdout
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
...     tableformat.print_table(portfolio, ['name','shares','price'], formatter)
...     file.close()
...
>>> # Let's check the content of the output file
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

¡Genial! Nuestro gestor de contexto funcionó como se esperaba. Redirigió con éxito la salida de la tabla al archivo `out.txt`.

Los gestores de contexto son una característica muy poderosa en Python. Te ayudan a manejar recursos adecuadamente. Aquí hay algunos casos de uso comunes para los gestores de contexto:

- Operaciones de archivos: Cuando abres un archivo, un gestor de contexto puede asegurarse de que el archivo se cierre correctamente, incluso si ocurre un error.
- Conexiones a bases de datos: Puede garantizar que la conexión a la base de datos se cierre después de que hayas terminado de usarla.
- Bloqueos en programas con hilos: Los gestores de contexto pueden manejar el bloqueo y desbloqueo de recursos de manera segura.
- Cambio temporal de configuraciones de entorno: Puedes cambiar algunas configuraciones para un bloque de código y luego restaurarlas automáticamente.

Este patrón es muy importante porque asegura que los recursos se limpien adecuadamente, incluso si ocurre una excepción dentro del bloque `with`.

Cuando hayas terminado de probar, puedes salir del intérprete de Python:

```python
>>> exit()
```
