# Comprendiendo la asignación de memoria de las listas

En Python, las listas son una estructura de datos muy útil, especialmente cuando necesitas agregar elementos a ellas. Las listas de Python están diseñadas para ser eficientes en las operaciones de anexión. En lugar de asignar exactamente la cantidad de memoria necesaria, Python asigna memoria adicional anticipando futuras adiciones. Esta estrategia minimiza la cantidad de reasignaciones de memoria necesarias cuando la lista crece.

Comprendamos mejor este concepto utilizando la función `sys.getsizeof()`. Esta función devuelve el tamaño de un objeto en bytes, lo que nos ayuda a ver cuánta memoria está utilizando una lista en diferentes etapas.

1. Primero, necesitas abrir una shell interactiva de Python en tu terminal. Esto es como un espacio de prueba donde puedes ejecutar código de Python de inmediato. Para abrirla, escribe el siguiente comando en tu terminal y presiona Enter:

```bash
python3
```

2. Una vez que estés en la shell interactiva de Python, necesitas importar el módulo `sys`. Los módulos en Python son como cajas de herramientas que contienen funciones útiles. El módulo `sys` tiene la función `getsizeof()` que necesitamos. Después de importar el módulo, crea una lista vacía llamada `items`. Aquí está el código para hacerlo:

```python
import sys
items = []
```

3. Ahora, veamos el tamaño inicial de la lista vacía. Usaremos la función `sys.getsizeof()` con la lista `items` como argumento. Escribe el siguiente código en la shell interactiva de Python y presiona Enter:

```python
sys.getsizeof(items)
```

Deberías ver un valor como `64` bytes. Este valor representa la sobrecarga de una lista vacía. La sobrecarga es la cantidad básica de memoria que Python utiliza para gestionar la lista, incluso cuando no tiene elementos.

4. A continuación, comenzaremos a agregar elementos a la lista uno por uno y observaremos cómo cambia la asignación de memoria. Usaremos el método `append()` para agregar un elemento a la lista y luego comprobaremos el tamaño nuevamente. Aquí está el código:

```python
items.append(1)
sys.getsizeof(items)
```

Deberías ver un valor mayor, alrededor de `96` bytes. Este aumento de tamaño muestra que Python ha asignado más memoria para acomodar el nuevo elemento.

5. Continuemos agregando más elementos a la lista y comprobemos el tamaño después de cada adición. Aquí está el código para hacerlo:

```python
items.append(2)
sys.getsizeof(items)  # El tamaño sigue siendo el mismo

items.append(3)
sys.getsizeof(items)  # El tamaño sigue sin cambiar

items.append(4)
sys.getsizeof(items)  # El tamaño sigue sin cambiar

items.append(5)
sys.getsizeof(items)  # El tamaño salta a un valor mayor
```

Notarás que el tamaño no aumenta con cada operación de anexión. En lugar de eso, aumenta periódicamente. Esto demuestra que Python está asignando memoria en bloques en lugar de individualmente para cada nuevo elemento.

Este comportamiento es intencional. Python asigna más memoria de la necesaria inicialmente para evitar reasignaciones frecuentes a medida que la lista crece. Cada vez que la lista supera su capacidad actual, Python asigna un bloque de memoria más grande.

Recuerda que una lista almacena referencias a objetos, no los objetos en sí. En un sistema de 64 bits, cada referencia generalmente requiere 8 bytes de memoria. Esto es importante de entender porque afecta cuánta memoria realmente utiliza una lista cuando contiene diferentes tipos de objetos.
