# Creando objetos Stock

Ahora que hemos definido nuestra clase `Stock`, es hora de ponerla en acción. Crear instancias de una clase es como hacer ejemplos específicos basados en un modelo general. En este caso, la clase `Stock` es nuestro modelo, y crearemos algunos objetos de acciones. Después de crear estos objetos, aprenderemos cómo acceder a sus atributos (características) y métodos (acciones que pueden realizar).

1. Primero, necesitamos abrir una terminal en el WebIDE. La terminal es como un centro de comandos donde podemos dar instrucciones a nuestra computadora. Para abrirla, haz clic en "Terminal" en el menú.

2. Una vez que la terminal esté abierta, debemos asegurarnos de estar en el directorio correcto del proyecto. El directorio del proyecto es donde se almacenan todos los archivos relevantes para nuestro proyecto. Si no estás ya en el directorio del proyecto, utiliza el siguiente comando para navegar hasta allí:

```bash
cd /home/labex/project
```

3. Ahora, queremos iniciar Python en modo interactivo con nuestro archivo `stock.py`. El modo interactivo nos permite probar nuestro código paso a paso y ver los resultados inmediatamente. El archivo `stock.py` contiene la definición de nuestra clase `Stock`. Utiliza el siguiente comando:

```bash
python3 -i stock.py
```

La bandera `-i` es importante aquí. Le dice a Python que ejecute primero el script `stock.py`. Después de ejecutar el script, inicia una sesión interactiva. En esta sesión, podemos acceder a cualquier clase y variable que se hayan definido en el script `stock.py`.

4. Creemos un nuevo objeto `Stock` para las acciones de Google. Crear un objeto es como hacer una instancia específica de la clase `Stock` con valores particulares. Utiliza el siguiente código:

```python
s = Stock('GOOG', 100, 490.10)
```

Esta línea de código crea una nueva instancia de la clase `Stock`. Aquí está lo que significa cada valor:

- Nombre: 'GOOG' - Este es el símbolo de las acciones de Google.
- Acciones: 100 - Representa el número de acciones de Google que tenemos.
- Precio: 490.10 - Este es el precio por acción de las acciones de Google.

5. Ahora que tenemos nuestro objeto `Stock`, podemos acceder a sus atributos. Los atributos son como las propiedades de un objeto. Para acceder a un atributo, usamos el nombre del objeto seguido de un punto y el nombre del atributo.

```python
s.name
```

Cuando ejecutes este código, mostrará el nombre de la acción:

```
'GOOG'
```

Accedamos al número de acciones:

```python
s.shares
```

La salida será el número de acciones que definimos:

```
100
```

Finalmente, accedamos al precio por acción:

```python
s.price
```

La salida será el precio por acción:

```
490.1
```

6. Nuestra clase `Stock` tiene un método llamado `cost()`. Un método es como una acción que un objeto puede realizar. En este caso, el método `cost()` calcula el costo total de nuestras acciones. Para llamar a este método, utiliza el siguiente código:

```python
s.cost()
```

La salida será el costo total:

```
49010.0
```

El método `cost()` funciona multiplicando el número de acciones (100) por el precio por acción (490.10), lo que nos da 49010.0.
