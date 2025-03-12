# Mejorando la tubería de corrutinas

Ahora que tenemos una tubería básica funcionando, es hora de hacerla más flexible. En programación, la flexibilidad es crucial ya que permite que nuestro código se adapte a diferentes requisitos. Lo lograremos modificando nuestro programa `coticker.py` para soportar diversas opciones de filtrado y formato.

1. Primero, abre el archivo `coticker.py` en tu editor de código. El editor de código es donde realizarás todos los cambios necesarios en el programa. Proporciona un entorno conveniente para ver, editar y guardar tu código.

2. A continuación, agregaremos una nueva corrutina que filtra los datos por el nombre de la acción. Una corrutina es un tipo especial de función que puede pausar y reanudar su ejecución. Esto nos permite crear una tubería donde los datos pueden fluir a través de diferentes pasos de procesamiento. Aquí está el código de la nueva corrutina:

```python
@consumer
def filter_by_name(name, target):
    while True:
        record = yield
        if record.name == name:
            target.send(record)
```

En este código, la corrutina `filter_by_name` toma un nombre de acción y una corrutina objetivo como parámetros. Espera continuamente un registro utilizando la palabra clave `yield`. Cuando llega un registro, comprueba si el nombre del registro coincide con el nombre especificado. Si coincide, envía el registro a la corrutina objetivo.

3. Ahora, agreguemos otra corrutina que filtre en base a umbrales de precio. Esta corrutina nos ayudará a seleccionar acciones dentro de un rango de precios específico. Aquí está el código:

```python
@consumer
def price_threshold(min_price, max_price, target):
    while True:
        record = yield
        if min_price <= record.price <= max_price:
            target.send(record)
```

Similar a la corrutina anterior, la corrutina `price_threshold` espera un registro. Luego comprueba si el precio del registro está dentro del rango de precio mínimo y máximo especificado. Si lo está, envía el registro a la corrutina objetivo.

4. Después de agregar las nuevas corrutinas, necesitamos actualizar el programa principal para demostrar estos filtros adicionales. El programa principal es el punto de entrada de nuestra aplicación, donde configuramos las tuberías de procesamiento y comenzamos el flujo de datos. Aquí está el código actualizado:

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change', 'high', 'low']

    # Create the processing pipeline with multiple outputs

    # Pipeline 1: Show all negative changes (same as before)
    print("Stocks with negative changes:")
    t1 = ticker('text', fields)
    neg_filter = negchange(t1)
    tick_creator1 = create_ticker(neg_filter)
    csv_parser1 = to_csv(tick_creator1)

    # Start following the file with the first pipeline
    import threading
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser1), daemon=True).start()

    # Wait a moment to see some results
    import time
    time.sleep(5)

    # Pipeline 2: Filter by name (AAPL)
    print("\nApple stock updates:")
    t2 = ticker('text', fields)
    name_filter = filter_by_name('AAPL', t2)
    tick_creator2 = create_ticker(name_filter)
    csv_parser2 = to_csv(tick_creator2)

    # Follow the file with the second pipeline
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser2), daemon=True).start()

    # Wait a moment to see some results
    time.sleep(5)

    # Pipeline 3: Filter by price range
    print("\nStocks priced between 50 and 75:")
    t3 = ticker('text', fields)
    price_filter = price_threshold(50, 75, t3)
    tick_creator3 = create_ticker(price_filter)
    csv_parser3 = to_csv(tick_creator3)

    # Follow with the third pipeline
    follow('stocklog.csv', csv_parser3)
```

En este código actualizado, creamos tres tuberías de procesamiento diferentes. La primera tubería muestra las acciones con cambios negativos, la segunda tubería filtra las acciones por el nombre 'AAPL' y la tercera tubería filtra las acciones en base a un rango de precios entre 50 y 75. Usamos hilos para ejecutar las dos primeras tuberías de forma concurrente, lo que nos permite procesar los datos de manera más eficiente.

5. Una vez que hayas realizado todos los cambios, guarda el archivo. Guardar el archivo asegura que todas tus modificaciones se conserven. Luego, ejecuta el programa actualizado utilizando los siguientes comandos en tu terminal:

```bash
cd /home/labex/project
python3 coticker.py
```

El comando `cd` cambia el directorio actual al directorio del proyecto, y el comando `python3 coticker.py` ejecuta el programa de Python.

6. Después de ejecutar el programa, deberías ver tres salidas diferentes:
   - Primero, verás las acciones con cambios negativos.
   - Luego, verás todas las actualizaciones de las acciones de AAPL.
   - Finalmente, verás todas las acciones con precios entre 50 y 75.

## Comprendiendo la tubería mejorada

El programa mejorado demuestra varios conceptos importantes:

1. **Múltiples tuberías**: Podemos crear múltiples tuberías de procesamiento a partir de la misma fuente de datos. Esto nos permite realizar diferentes tipos de análisis en los mismos datos simultáneamente.
2. **Filtros especializados**: Podemos crear diferentes corrutinas para tareas de filtrado específicas. Estos filtros nos ayudan a seleccionar solo los datos que cumplen con nuestros criterios específicos.
3. **Procesamiento concurrente**: Usando hilos, podemos ejecutar múltiples tuberías de forma concurrente. Esto mejora la eficiencia de nuestro programa al permitirle procesar datos en paralelo.
4. **Composición de tuberías**: Las corrutinas se pueden combinar de diferentes maneras para alcanzar diferentes objetivos de procesamiento de datos. Esto nos da la flexibilidad de personalizar nuestras tuberías de procesamiento de datos según nuestras necesidades.

Este enfoque proporciona una forma flexible y modular de procesar datos en streaming. Permite agregar o modificar pasos de procesamiento sin cambiar la arquitectura general del programa.
