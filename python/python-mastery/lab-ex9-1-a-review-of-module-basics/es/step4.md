# Utilizando la sintaxis from module import

En Python, hay varias formas de importar componentes de módulos. Una de estas formas es la sintaxis `from module import`, que exploraremos en esta sección.

Cuando importas componentes de un módulo, a menudo es una buena idea comenzar con un entorno limpio. Esto asegura que no haya variables o configuraciones residuales de interacciones previas que puedan interferir con nuestro experimento actual.

1. Reinicia el intérprete de Python para obtener un estado limpio:

```python
>>> exit()
```

Este comando sale de la sesión actual del intérprete de Python. Después de salir, iniciaremos una nueva sesión para garantizar un entorno nuevo.

```bash
python3
```

Este comando de bash inicia una nueva sesión del intérprete de Python 3. Ahora que tenemos un entorno de Python limpio, podemos comenzar a importar componentes de un módulo.

2. Importa componentes específicos de un módulo utilizando la sintaxis `from module import`:

```python
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
```

Aquí, estamos utilizando la declaración `from simplemod import foo` para importar solo la función `foo` del módulo `simplemod`. Observa que aunque solo pedimos la función `foo`, se cargó el módulo `simplemod` completo. Esto se indica por la salida "Loaded simplemod". La razón de esto es que Python necesita cargar todo el módulo para acceder a la función `foo`.

3. Cuando se utiliza `from module import`, no se puede acceder al módulo en sí:

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
```

Cuando utilizamos la sintaxis `from module import`, solo estamos trayendo los componentes especificados directamente a nuestro espacio de nombres. El nombre del módulo en sí no se importa. Entonces, cuando intentamos acceder a `simplemod.foo()`, Python no reconoce `simplemod` porque no se importó de esa manera.

4. Puedes importar múltiples componentes a la vez:

```python
>>> from simplemod import x, foo
>>> x
42
>>> foo()
x is 42
```

La sintaxis `from module import` nos permite importar múltiples componentes de un módulo en una sola declaración. Aquí, estamos importando tanto la variable `x` como la función `foo` del módulo `simplemod`. Después de importarlos, podemos acceder directamente a estos componentes en nuestro código.

5. Cuando importas una variable de un módulo, estás creando una nueva referencia al objeto, no un enlace a la variable en el módulo:

```python
>>> x = 13  # Change the local variable x
>>> x
13
>>> foo()
x is 42  # The function still uses the module's x, not your local x
```

Cuando importamos una variable de un módulo, en esencia estamos creando una nueva referencia al mismo objeto en nuestro espacio de nombres local. Entonces, cuando cambiamos la variable local `x` a `13`, no afecta a la variable `x` dentro del módulo `simplemod`. La función `foo()` sigue refiriéndose a la variable `x` del módulo, que es `42`. Comprender este concepto es crucial para evitar confusiones en tu código.