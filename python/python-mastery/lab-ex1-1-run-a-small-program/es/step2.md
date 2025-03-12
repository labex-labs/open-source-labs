# Crear un programa simple de Python

Ahora que hemos confirmado que Python está funcionando correctamente, es hora de crear nuestro primer archivo de programa de Python. Para los principiantes, siempre es una buena idea comenzar con algo simple antes de pasar a programas más complejos. De esta manera, puedes entender gradualmente los conceptos básicos y la sintaxis de Python.

## Crear tu primer archivo de Python

Primero, crearemos un nuevo archivo de Python. Así es como puedes hacerlo:

1. En el WebIDE, notarás un panel en el lado izquierdo de la pantalla llamado panel del Explorador. Este panel te ayuda a navegar por diferentes archivos y directorios en tu proyecto. Encuentra este panel.

2. Una vez que hayas encontrado el panel del Explorador, necesitas navegar al directorio `/home/labex/project`. Aquí es donde almacenaremos nuestro programa de Python.

3. Haz clic derecho en cualquier lugar del panel del Explorador. Aparecerá un menú. Desde este menú, selecciona "Nuevo archivo". Esta acción creará un nuevo archivo vacío.

4. Después de crear el nuevo archivo, necesitas darle un nombre. Nombrar el archivo `hello.py`. En Python, los archivos suelen tener la extensión `.py`, que indica que contienen código de Python.

5. Ahora, abre el recién creado archivo `hello.py` en el editor. En el editor, escribe el siguiente código:

   ```python
   # This is a simple Python program

   name = input("Enter your name: ")
   print(f"Hello, {name}! Welcome to Python programming.")
   ```

   Analicemos este código. La línea que comienza con `#` es un comentario. Los comentarios se utilizan para explicar lo que hace el código y son ignorados por el intérprete de Python. La función `input()` se utiliza para obtener la entrada del usuario. Muestra el mensaje "Enter your name: " y espera a que el usuario escriba algo. El valor ingresado por el usuario se almacena luego en la variable `name`. La función `print()` se utiliza para mostrar la salida en la pantalla. La `f"Hello, {name}!"` es una f-string, que es una forma conveniente de formatear cadenas en Python. Te permite insertar el valor de una variable directamente en una cadena.

6. Después de escribir el código, necesitas guardar el archivo. Puedes hacerlo presionando Ctrl+S en tu teclado o seleccionando Archivo > Guardar desde el menú. Guardar el archivo asegura que tus cambios se conserven.

## Ejecutar tu primer programa de Python

Ahora que has creado y guardado tu programa de Python, es hora de ejecutarlo. Así es como se hace:

1. Abre una terminal en el WebIDE si no está abierta. La terminal te permite ejecutar comandos y programas.

2. Antes de ejecutar el programa de Python, necesitas asegurarte de que estás en el directorio correcto. Escribe el siguiente comando en la terminal:

   ```bash
   cd ~/project
   ```

   Este comando cambia el directorio de trabajo actual al directorio `project` en tu directorio principal.

3. Una vez que estés en el directorio correcto, puedes ejecutar tu programa de Python. Escribe el siguiente comando en la terminal:

   ```bash
   python3 hello.py
   ```

   Este comando le dice al intérprete de Python que ejecute el archivo `hello.py`.

4. Cuando se ejecute el programa, te pedirá que ingreses tu nombre. Escribe tu nombre y presiona Enter.

5. Después de presionar Enter, deberías ver una salida similar a:

   ```
   Enter your name: John
   Hello, John! Welcome to Python programming.
   ```

   La salida real mostrará el nombre que ingresaste en lugar de "John".

Este programa simple demuestra varios conceptos importantes en Python:

- Crear un archivo de Python: Aprendiste cómo crear un nuevo archivo de Python en el WebIDE.
- Agregar comentarios: Los comentarios se utilizan para explicar el código y hacerlo más comprensible.
- Obtener la entrada del usuario con la función `input()`: Esta función permite que tu programa interactúe con el usuario.
- Usar variables para almacenar datos: Las variables se utilizan para almacenar valores que se pueden utilizar más adelante en el programa.
- Mostrar la salida con la función `print()`: Esta función se utiliza para mostrar información en la pantalla.
- Usar f-strings para el formato de cadenas: Las f-strings proporcionan una forma conveniente de insertar variables en cadenas.
