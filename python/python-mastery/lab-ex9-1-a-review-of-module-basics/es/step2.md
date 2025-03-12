# Importación y uso de módulos

Ahora que hemos creado un módulo, es hora de entender cómo importarlo y utilizar sus componentes. En Python, un módulo es un archivo que contiene definiciones y declaraciones de Python. Cuando importas un módulo, obtienes acceso a todas las funciones, clases y variables definidas en él. Esto te permite reutilizar código y organizar tus programas de manera más efectiva.

1. Primero, necesitamos abrir una nueva terminal en el WebIDE. Esta terminal servirá como nuestro espacio de trabajo donde podemos ejecutar comandos de Python. Para abrir una nueva terminal, haz clic en "Terminal" > "New Terminal".

2. Una vez abierta la terminal, necesitamos iniciar el intérprete de Python. El intérprete de Python es un programa que lee y ejecuta código de Python. Para iniciarlo, escribe el siguiente comando en la terminal y presiona Enter:

```bash
python3
```

3. Ahora que el intérprete de Python está en funcionamiento, podemos importar nuestro módulo. En Python, usamos la declaración `import` para traer un módulo a nuestro programa actual. Escribe el siguiente comando en el intérprete de Python:

```python
>>> import simplemod
Loaded simplemod
```

Notarás que aparece "Loaded simplemod" en la salida. Esto se debe a que la declaración `print` en nuestro módulo `simplemod` se ejecuta cuando el módulo se carga. Cuando Python importa un módulo, ejecuta todo el código de nivel superior en ese módulo, incluyendo cualquier declaración `print`.

4. Después de importar el módulo, podemos acceder a sus componentes utilizando la notación de punto. La notación de punto es una forma de acceder a los atributos (variables y funciones) de un objeto en Python. En este caso, el módulo es un objeto, y sus funciones, variables y clases son sus atributos. Aquí hay algunos ejemplos de cómo acceder a diferentes componentes del módulo `simplemod`:

```python
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
>>> spam_instance = simplemod.Spam()
>>> spam_instance.yow()
Yow!
```

En la primera línea, accedemos a la variable `x` definida en el módulo `simplemod`. En la segunda línea, llamamos a la función `foo` del módulo `simplemod`. En la tercera y cuarta línea, creamos una instancia de la clase `Spam` definida en el módulo `simplemod` y llamamos a su método `yow`.

5. A veces, es posible que encuentres un `ImportError` cuando intentas importar un módulo. Este error se produce cuando Python no puede encontrar el módulo que estás intentando importar. Para averiguar dónde Python está buscando los módulos, puedes examinar la variable `sys.path`. La variable `sys.path` es una lista de directorios que Python busca cuando está buscando módulos. Escribe los siguientes comandos en el intérprete de Python:

```python
>>> import sys
>>> sys.path
['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
```

El primer elemento de la lista (la cadena vacía) representa el directorio de trabajo actual. Aquí es donde Python busca el archivo `simplemod.py`. Si tu módulo no está en uno de los directorios enumerados en `sys.path`, Python no podrá encontrarlo y obtendrás un `ImportError`. Asegúrate de que tu archivo `simplemod.py` esté en el directorio de trabajo actual o en uno de los otros directorios de `sys.path`.