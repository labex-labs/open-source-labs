# Asignación de memoria de los diccionarios

En Python, al igual que las listas, los diccionarios son una estructura de datos fundamental. Un aspecto importante que debes entender sobre ellos es cómo asignan memoria. La asignación de memoria se refiere a cómo Python reserva espacio en la memoria del ordenador para almacenar los datos de tu diccionario. Al igual que las listas, los diccionarios de Python también asignan memoria en bloques. Exploremos cómo funciona la asignación de memoria con los diccionarios.

1. Primero, necesitamos crear un diccionario con el que trabajar. En la misma shell de Python (o abre una nueva si la cerraste), crearemos un diccionario que represente un registro de datos. Un diccionario en Python es una colección de pares clave - valor, donde cada clave es única y se utiliza para acceder a su valor correspondiente.

```python
import sys  # Importa sys si estás comenzando una nueva sesión
row = {'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

Aquí, hemos importado el módulo `sys` que proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete de Python y a funciones que interactúan fuertemente con el intérprete. Luego, creamos un diccionario llamado `row` con cuatro pares clave - valor.

2. Ahora que tenemos nuestro diccionario, queremos comprobar su tamaño inicial. El tamaño de un diccionario se refiere a la cantidad de memoria que ocupa en el ordenador.

```python
sys.getsizeof(row)
```

La función `sys.getsizeof()` devuelve el tamaño de un objeto en bytes. Cuando ejecutes este código, deberías ver un valor alrededor de `240` bytes. Esto te da una idea de cuánta memoria ocupa el diccionario inicialmente.

3. A continuación, agregaremos nuevos pares clave - valor al diccionario y observaremos cómo cambia la asignación de memoria. Agregar elementos a un diccionario es una operación común, y entender cómo afecta a la memoria es crucial.

```python
row['a'] = 1
sys.getsizeof(row)  # El tamaño puede permanecer igual

row['b'] = 2
sys.getsizeof(row)  # El tamaño puede aumentar
```

Cuando agregas el primer par clave - valor (`'a': 1`), el tamaño del diccionario puede permanecer igual. Esto se debe a que Python ya ha asignado un cierto bloque de memoria, y puede haber suficiente espacio en ese bloque para acomodar el nuevo elemento. Sin embargo, cuando agregas el segundo par clave - valor (`'b': 2`), el tamaño puede aumentar. Notarás que después de agregar un cierto número de elementos, el tamaño del diccionario aumenta repentinamente. Esto se debe a que los diccionarios, como las listas, asignan memoria en bloques para optimizar el rendimiento. Asignar memoria en bloques reduce la cantidad de veces que Python tiene que solicitar más memoria al sistema, lo que acelera el proceso de agregar nuevos elementos.

4. Intentemos eliminar un elemento del diccionario para ver si el uso de memoria disminuye. Eliminar elementos de un diccionario también es una operación común, y es interesante ver cómo afecta a la memoria.

```python
del row['b']
sys.getsizeof(row)
```

Curiosamente, eliminar un elemento generalmente no reduce la asignación de memoria. Esto se debe a que Python conserva la memoria asignada para evitar reasignarla si se agregan elementos nuevamente. Reasignar memoria es una operación relativamente costosa en términos de rendimiento, por lo que Python intenta evitarla tanto como sea posible.

**Consideraciones sobre la eficiencia de memoria:**

Cuando trabajas con grandes conjuntos de datos donde necesitas crear muchos registros, usar diccionarios para cada registro puede no ser el enfoque más eficiente en términos de memoria. Los diccionarios son muy flexibles y fáciles de usar, pero pueden consumir una cantidad significativa de memoria, especialmente cuando se trata de un gran número de registros. Aquí hay algunas alternativas que consumen menos memoria:

- Tuplas: Secuencias inmutables simples. Una tupla es una colección de valores que no se pueden cambiar después de su creación. Utiliza menos memoria que un diccionario porque no necesita almacenar claves ni gestionar la correspondiente asignación clave - valor.
- Tuplas con nombres (Named tuples): Tuplas con nombres de campos. Las tuplas con nombres son similares a las tuplas normales, pero te permiten acceder a los valores por nombre, lo que puede hacer el código más legible. También utilizan menos memoria que los diccionarios.
- Clases con `__slots__`: Clases que definen explícitamente atributos para evitar usar un diccionario para las variables de instancia. Cuando se utiliza `__slots__` en una clase, Python no crea un diccionario para almacenar las variables de instancia, lo que reduce el uso de memoria.

Estas alternativas pueden reducir significativamente el uso de memoria cuando se manejan muchos registros.
