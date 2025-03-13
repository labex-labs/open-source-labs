# Comprendiendo el comportamiento de carga de módulos

En Python, la forma en que se cargan los módulos tiene algunas características interesantes. En este paso, exploraremos estos comportamientos para entender cómo Python gestiona la carga de módulos.

1. Primero, veamos qué sucede cuando intentamos importar un módulo nuevamente dentro de la misma sesión del intérprete de Python. Cuando inicias un intérprete de Python, es como abrir un espacio de trabajo donde puedes ejecutar código de Python. Una vez que has importado un módulo, importarlo nuevamente podría parecer que recargaría el módulo, pero no es así.

```python
>>> import simplemod
```

Observa que esta vez no ves la salida "Loaded simplemod". Esto se debe a que **Python solo carga un módulo una vez** por sesión del intérprete. Las declaraciones `import` subsiguientes no recargan el módulo. Python recuerda que ya ha cargado el módulo, por lo que no pasa por el proceso de cargarlo nuevamente.

2. Después de importar un módulo, puedes modificar las variables dentro de él. Un módulo en Python es como un contenedor que almacena variables, funciones y clases. Una vez que has importado un módulo, puedes acceder y cambiar sus variables al igual que con cualquier otro objeto de Python.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> simplemod.foo()
x is 13
```

Aquí, primero comprobamos el valor de la variable `x` en el módulo `simplemod`, que inicialmente es `42`. Luego cambiamos su valor a `13` y verificamos que se haya realizado el cambio. Cuando llamamos a la función `foo` en el módulo, se refleja el nuevo valor de `x`.

3. Importar el módulo nuevamente no restablece los cambios que hicimos en sus variables. Incluso si intentamos importar el módulo una vez más, Python no lo recarga, por lo que los cambios que hicimos en sus variables se mantienen.

```python
>>> import simplemod
>>> simplemod.x
13
```

4. Si quieres forzar la recarga de un módulo, necesitas usar la función `importlib.reload()`. A veces, es posible que hayas realizado cambios en el código del módulo y quieras ver que esos cambios surtan efecto inmediatamente. La función `importlib.reload()` te permite hacer precisamente eso.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
```

El módulo se ha recargado y el valor de `x` se ha restablecido a `42`. Esto muestra que el módulo se ha cargado nuevamente desde su código fuente y todas las variables se han inicializado como estaban originalmente.

5. Python lleva un registro de todos los módulos cargados en el diccionario `sys.modules`. Este diccionario actúa como un registro donde Python almacena información sobre todos los módulos que se han cargado durante la sesión actual del intérprete.

```python
>>> 'simplemod' in sys.modules
True
>>> sys.modules['simplemod']
<module 'simplemod' from 'simplemod.py'>
```

Al comprobar si un nombre de módulo está en el diccionario `sys.modules`, puedes ver si el módulo se ha cargado. Y al acceder al diccionario con el nombre del módulo como clave, puedes obtener información sobre el módulo.

6. Puedes eliminar un módulo de este diccionario para forzar a Python a recargarlo en la próxima importación. Si eliminas un módulo del diccionario `sys.modules`, Python olvida que ya ha cargado el módulo. Entonces, la próxima vez que intentes importarlo, Python lo cargará nuevamente desde su código fuente.

```python
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>> simplemod.x
42
```

El módulo se cargó nuevamente porque se eliminó de `sys.modules`. Esta es otra forma de asegurarte de que estás trabajando con la última versión del código de un módulo.