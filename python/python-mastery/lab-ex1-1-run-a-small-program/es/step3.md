# Crear un programa de Python más avanzado

Ahora que has dominado los conceptos básicos de Python, es hora de dar el siguiente paso y crear un programa de Python más avanzado. Este programa generará patrones de arte ASCII, que son diseños simples pero visualmente interesantes formados por caracteres de texto. Al trabajar en este programa, aprenderás y aplicarás varios conceptos importantes de Python, como importar módulos, definir funciones y manejar argumentos de línea de comandos.

## Crear el programa de arte ASCII

1. Primero, necesitamos abrir el archivo `art.py` en el WebIDE. Este archivo se creó durante el proceso de configuración. Lo puedes encontrar en el directorio `/home/labex/project`. Abrir este archivo es el punto de partida para escribir nuestro programa de arte ASCII.

2. Una vez que el archivo esté abierto, notarás que puede tener algún contenido existente. Necesitamos borrarlo porque vamos a escribir nuestro propio código desde cero. Así que, borra cualquier contenido existente en el archivo. Luego, copia el siguiente código en el archivo `art.py`. Este código es el núcleo de nuestro generador de arte ASCII.

   ```python
   # art.py - A program to generate ASCII art patterns

   import sys
   import random

   # Characters used for the art pattern
   chars = '\|/'

   def draw(rows, columns):
       """
       Generate and print an ASCII art pattern with the specified dimensions.

       Args:
           rows: Number of rows in the pattern
           columns: Number of columns in the pattern
       """
       for r in range(rows):
           # For each row, create a string of random characters
           line = ''.join(random.choice(chars) for _ in range(columns))
           print(line)

   # This code only runs when the script is executed directly
   if __name__ == '__main__':
       # Check if the correct number of arguments was provided
       if len(sys.argv) != 3:
           print("Error: Incorrect number of arguments")
           print("Usage: python3 art.py rows columns")
           print("Example: python3 art.py 10 20")
           sys.exit(1)

       try:
           # Convert the arguments to integers
           rows = int(sys.argv[1])
           columns = int(sys.argv[2])

           # Call the draw function with the specified dimensions
           draw(rows, columns)
       except ValueError:
           print("Error: Both arguments must be integers")
           sys.exit(1)
   ```

3. Después de copiar el código en el archivo, es importante guardar tu trabajo. Puedes hacerlo presionando Ctrl + S en tu teclado. Alternativamente, puedes ir al menú y seleccionar Archivo > Guardar. Guardar el archivo asegura que tu código se almacene y esté listo para ser ejecutado.

## Entendiendo el código

Echemos un vistazo más de cerca a lo que hace este programa. Entender el código es crucial para que puedas modificar y expandirlo en el futuro.

- **Declaraciones de importación**: Las líneas `import sys` e `import random` se utilizan para importar módulos incorporados de Python. El módulo `sys` proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete de Python y a funciones que interactúan fuertemente con el intérprete. El módulo `random` nos permite generar números aleatorios, que usaremos para crear patrones de arte ASCII aleatorios.
- **Conjunto de caracteres**: La línea `chars = '\|/'` define el conjunto de caracteres que se utilizarán para crear nuestro arte ASCII. Estos caracteres se seleccionarán aleatoriamente para formar los patrones.
- **La función `draw()`**: Esta función es responsable de crear los patrones de arte ASCII. Toma dos argumentos, `rows` y `columns`, que especifican las dimensiones del patrón. Dentro de la función, utiliza un bucle para crear cada fila del patrón seleccionando aleatoriamente caracteres del conjunto `chars`.
- **Bloque principal**: El bloque `if __name__ == '__main__':` es una construcción especial en Python. Asegura que el código dentro de este bloque solo se ejecute cuando se ejecuta directamente el archivo `art.py`. Si el archivo se importa a otro archivo de Python, este código no se ejecutará.
- **Manejo de argumentos**: La variable `sys.argv` contiene los argumentos de línea de comandos pasados al programa. Comprobamos si se proporcionan exactamente 3 argumentos (el nombre del script en sí más dos números que representan el número de filas y columnas). Esto nos ayuda a asegurarnos de que el usuario proporciona la entrada correcta.
- **Manejo de errores**: El bloque `try/except` se utiliza para capturar errores que pueden ocurrir. Si el usuario proporciona entradas no válidas, como valores no enteros para las filas y columnas, el bloque `try` generará un `ValueError`, y el bloque `except` imprimirá un mensaje de error y saldrá del programa.

## Ejecutar el programa

1. Para ejecutar nuestro programa, primero necesitamos abrir una terminal en el WebIDE. En la terminal es donde ingresaremos los comandos para ejecutar nuestro script de Python.

2. Una vez que la terminal esté abierta, necesitamos navegar al directorio del proyecto. Aquí es donde se encuentra nuestro archivo `art.py`. Utiliza el siguiente comando en la terminal:

   ```bash
   cd ~/project
   ```

   Este comando cambia el directorio de trabajo actual al directorio del proyecto.

3. Ahora que estamos en el directorio correcto, podemos ejecutar el programa. Utiliza el siguiente comando:

   ```bash
   python3 art.py 5 10
   ```

   Este comando le dice a Python que ejecute el script `art.py` con 5 filas y 10 columnas. Cuando ejecutes este comando, verás un patrón de caracteres de 5×10 impreso en la terminal. La salida se verá algo así:

   ```
   |\//\\|\//
   /\\|\|//\\
   \\\/\|/|/\
   //|\\\||\|
   \|//|/\|/\
   ```

   Recuerda, el patrón real es aleatorio, así que tu salida será diferente del ejemplo mostrado aquí.

4. Puedes experimentar con diferentes dimensiones cambiando los argumentos en el comando. Por ejemplo, prueba el siguiente comando:

   ```bash
   python3 art.py 8 15
   ```

   Esto generará un patrón más grande con 8 filas y 15 columnas.

5. Para ver el manejo de errores en acción, intenta proporcionar argumentos no válidos. Ejecuta el siguiente comando:

   ```bash
   python3 art.py
   ```

   Deberías ver un mensaje de error como este:

   ```
   Error: Incorrect number of arguments
   Usage: python3 art.py rows columns
   Example: python3 art.py 10 20
   ```

## Experimentar con el código

Puedes hacer los patrones de arte ASCII más interesantes modificando el conjunto de caracteres. Así es como puedes hacerlo:

1. Abre nuevamente el archivo `art.py` en el editor. Aquí es donde realizaremos los cambios en el código.

2. Encuentra la variable `chars` en el código. Cámbiala para usar diferentes caracteres. Por ejemplo, puedes usar el siguiente código:

   ```python
   chars = '*#@+.'
   ```

   Esto cambiará el conjunto de caracteres utilizados para crear el arte ASCII.

3. Después de hacer el cambio, guarda el archivo nuevamente utilizando Ctrl + S o Archivo > Guardar. Luego, ejecuta el programa con el siguiente comando:

   ```bash
   python3 art.py 5 10
   ```

   Ahora verás un patrón diferente utilizando tus nuevos caracteres.

Este ejercicio demuestra varios conceptos importantes de Python, incluyendo:

- Importación de módulos: Cómo importar funcionalidad adicional de los módulos incorporados de Python.
- Definición de funciones: Cómo definir y usar funciones para organizar tu código.
- Manejo de argumentos de línea de comandos: Cómo aceptar y procesar la entrada del usuario desde la línea de comandos.
- Manejo de errores con try/except: Cómo manejar los errores de manera elegante en tu programa.
- Manipulación de cadenas: Cómo crear y manipular cadenas para formar los patrones de arte ASCII.
- Generación de números aleatorios: Cómo generar valores aleatorios para crear patrones únicos.
- Comprensiones de listas: Una forma concisa de crear listas en Python, que se utiliza en la función `draw()`.
