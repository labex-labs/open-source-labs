# Verificar la instalación de Python y usar el intérprete interactivo

El intérprete interactivo de Python es una herramienta muy útil. Te permite ejecutar código de Python línea por línea y ver los resultados de inmediato. Esto es genial para los principiantes porque puedes probar pequeños fragmentos de código sin tener que escribir un programa completo. Antes de comenzar a escribir programas completos, necesitamos asegurarnos de que Python esté instalado correctamente en tu sistema. Luego, aprenderemos cómo usar este intérprete para ejecutar código de Python.

## Iniciar el intérprete de Python

1. Primero, necesitamos abrir una terminal en el WebIDE. La terminal es como un centro de comandos donde puedes escribir comandos para interactuar con tu computadora. Encontrarás una pestaña de terminal en la parte inferior de la pantalla. Una vez que la abras, estarás listo para comenzar a escribir comandos.

2. En la terminal, vamos a comprobar si Python está instalado y qué versión tienes. Escribe el siguiente comando y luego presiona Enter:

   ```bash
   python3 --version
   ```

   Este comando le pide a tu sistema que muestre la versión de Python que está actualmente instalada. Si Python está instalado correctamente, verás una salida similar a:

   ```
   Python 3.10.x
   ```

   La `x` aquí representa un número de parche específico, que puede variar dependiendo de tu instalación.

3. Ahora que sabemos que Python está instalado, comencemos el intérprete interactivo de Python. Escribe el siguiente comando en la terminal y presiona Enter:

   ```bash
   python3
   ```

   Después de presionar Enter, verás alguna información sobre la versión de Python y otros detalles. La salida se verá algo así:

   ```
   Python 3.10.x (default, ...)
   [GCC x.x.x] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```

   El indicador `>>>` es una señal de que el intérprete de Python está funcionando y está esperando que ingreses comandos de Python.

## Probar comandos simples de Python

Ahora que el intérprete de Python está en funcionamiento, probemos algunos comandos básicos de Python. Estos comandos te ayudarán a entender cómo funciona Python y cómo usar el intérprete.

1. En el indicador `>>>` , escribe el siguiente comando y presiona Enter:

   ```python
   >>> print('Hello World')
   ```

   La función `print` en Python se utiliza para mostrar texto en la pantalla. Cuando ejecutes este comando, verás la siguiente salida:

   ```
   Hello World
   >>>
   ```

   Esto muestra que la función `print` ha mostrado con éxito el texto 'Hello World'.

2. Probemos un cálculo matemático simple. En el indicador, escribe:

   ```python
   >>> 2 + 3
   ```

   Python evaluará automáticamente esta expresión y te mostrará el resultado. Verás:

   ```
   5
   >>>
   ```

   Esto demuestra que Python puede realizar operaciones aritméticas básicas.

3. A continuación, crearemos una variable y la usaremos. Las variables en Python se utilizan para almacenar datos. Escribe los siguientes comandos en el indicador:

   ```python
   >>> message = "Learning Python"
   >>> print(message)
   ```

   En la primera línea, estamos creando una variable llamada `message` y almacenando la cadena "Learning Python" en ella. En la segunda línea, estamos usando la función `print` para mostrar el valor almacenado en la variable `message`. La salida será:

   ```
   Learning Python
   >>>
   ```

   El intérprete de Python ejecuta cada línea de código tan pronto como la ingresas. Esto lo convierte en una gran herramienta para probar rápidamente ideas y aprender conceptos de Python.

## Salir del intérprete

Cuando hayas terminado de experimentar con el intérprete de Python, puedes salir de él utilizando uno de los siguientes métodos:

1. Puedes escribir el siguiente comando en el indicador `>>>` y presionar Enter:

   ```python
   >>> exit()
   ```

   O puedes usar este comando alternativo:

   ```python
   >>> quit()
   ```

   Ambos comandos le indican al intérprete de Python que deje de funcionar y te devuelva a la terminal normal.

2. Otra forma de salir es presionando Ctrl+D en tu teclado. Esta es una combinación de teclas que también detiene el intérprete de Python.

Después de salir del intérprete, volverás al indicador de la terminal normal, donde puedes ejecutar otros comandos en tu sistema.
