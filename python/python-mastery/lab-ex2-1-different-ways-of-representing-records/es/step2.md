# Medición del uso de memoria con diferentes métodos de almacenamiento

En este paso, vamos a ver cómo diferentes formas de almacenar datos pueden afectar el uso de memoria. El uso de memoria es un aspecto importante de la programación, especialmente cuando se trabaja con grandes conjuntos de datos. Para medir la memoria utilizada por nuestro código de Python, usaremos el módulo `tracemalloc` de Python. Este módulo es muy útil ya que nos permite realizar un seguimiento de las asignaciones de memoria realizadas por Python. Al usarlo, podemos ver cuánta memoria están consumiendo nuestros métodos de almacenamiento de datos.

## Método 1: Almacenar todo el archivo como una sola cadena

Comencemos creando un nuevo archivo de Python. Navega al directorio `/home/labex/project` y crea un archivo llamado `memory_test1.py`. Puedes usar un editor de texto para abrir este archivo. Una vez abierto el archivo, agrega el siguiente código. Este código leerá todo el contenido de un archivo como una sola cadena y medirá el uso de memoria.

```python
# memory_test1.py
import tracemalloc

def test_single_string():
    # Start tracking memory
    tracemalloc.start()

    # Read the entire file as a single string
    with open('/home/labex/project/ctabus.csv') as f:
        data = f.read()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"File length: {len(data)} characters")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_single_string()
```

Después de agregar el código, guarda el archivo. Ahora, para ejecutar este script, abre tu terminal y ejecuta el siguiente comando:

```bash
python3 /home/labex/project/memory_test1.py
```

Cuando ejecutes el script, deberías ver una salida similar a esta:

```
File length: 12361039 characters
Current memory usage: 11.80 MB
Peak memory usage: 23.58 MB
```

Los números exactos pueden ser diferentes en tu sistema, pero generalmente, notarás que el uso de memoria actual es de alrededor de 12 MB y el uso de memoria máximo es de aproximadamente 24 MB.

## Método 2: Almacenar como una lista de cadenas

A continuación, probaremos otra forma de almacenar los datos. Crea un nuevo archivo llamado `memory_test2.py` en el mismo directorio `/home/labex/project`. Abre este archivo en el editor y agrega el siguiente código. Este código lee el archivo y almacena cada línea como una cadena separada en una lista, y luego mide el uso de memoria.

```python
# memory_test2.py
import tracemalloc

def test_list_of_strings():
    # Start tracking memory
    tracemalloc.start()

    # Read the file as a list of strings (one string per line)
    with open('/home/labex/project/ctabus.csv') as f:
        lines = f.readlines()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"Number of lines: {len(lines)}")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_list_of_strings()
```

Guarda el archivo y luego ejecuta el script usando el siguiente comando en la terminal:

```bash
python3 /home/labex/project/memory_test2.py
```

Deberías ver una salida similar a esta:

```
Number of lines: 577564
Current memory usage: 43.70 MB
Peak memory usage: 43.74 MB
```

Observa que el uso de memoria ha aumentado significativamente en comparación con el método anterior de almacenar los datos como una sola cadena. Esto se debe a que cada línea en la lista es un objeto de cadena de Python separado, y cada objeto tiene su propio gasto de memoria.

## Entendiendo la diferencia de memoria

La diferencia en el uso de memoria entre los dos enfoques muestra un concepto importante en la programación de Python llamado gasto de objeto. Cuando almacenas datos como una lista de cadenas, cada cadena es un objeto de Python separado. Cada objeto tiene algunos requisitos de memoria adicionales, que incluyen:

1. El encabezado del objeto de Python (generalmente 16 - 24 bytes por objeto). Este encabezado contiene información sobre el objeto, como su tipo y el recuento de referencias.
2. La representación real de la cadena en sí, que almacena los caracteres de la cadena.
3. Relleno de alineación de memoria. Este es un espacio adicional agregado para garantizar que la dirección de memoria del objeto esté correctamente alineada para un acceso eficiente.

Por otro lado, cuando almacenas todo el contenido del archivo como una sola cadena, solo hay un objeto, y por lo tanto solo un conjunto de gastos. Esto lo hace más eficiente en términos de memoria cuando se considera el tamaño total de los datos.

Al diseñar programas que trabajen con grandes conjuntos de datos, debes considerar este compromiso entre la eficiencia de memoria y la accesibilidad de los datos. A veces, puede ser más conveniente acceder a los datos cuando se almacenan en una lista de cadenas, pero usará más memoria. En otras ocasiones, es posible que desees priorizar la eficiencia de memoria y optar por almacenar los datos como una sola cadena.
