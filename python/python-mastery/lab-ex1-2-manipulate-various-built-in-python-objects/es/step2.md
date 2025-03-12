# Trabajando con cadenas (strings) en Python

Las cadenas (strings) son uno de los tipos de datos más comúnmente utilizados en Python. Se utilizan para representar texto y pueden contener letras, números y símbolos. En este paso, exploraremos diversas operaciones con cadenas, que son habilidades esenciales para trabajar con datos de texto en Python.

## Creación y definición de cadenas

Para comenzar a trabajar con cadenas en Python, primero debemos abrir una shell interactiva de Python. Esta shell nos permite escribir y ejecutar código Python línea por línea, lo cual es excelente para aprender y probar. Abre una shell interactiva de Python nuevamente utilizando el siguiente comando:

```bash
python3
```

Una vez que la shell esté abierta, podemos definir una cadena. En este ejemplo, crearemos una cadena que contiene símbolos de acciones. Una cadena en Python se puede definir encerrando texto entre comillas simples (`'`) o comillas dobles (`"`). Así es como definimos nuestra cadena:

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
>>> symbols
'AAPL IBM MSFT YHOO SCO'
```

Ahora hemos creado una variable de cadena llamada `symbols` y le hemos asignado un valor. Cuando escribimos el nombre de la variable y presionamos enter, Python muestra el valor de la cadena.

## Acceso a caracteres y subcadenas

En Python, las cadenas se pueden indexar para acceder a caracteres individuales. La indexación comienza en 0, lo que significa que el primer carácter de una cadena tiene un índice de 0, el segundo tiene un índice de 1, y así sucesivamente. También se admite la indexación negativa, donde -1 se refiere al último carácter, -2 se refiere al penúltimo carácter, y así sucesivamente.

Veamos cómo podemos acceder a caracteres individuales en nuestra cadena `symbols`:

```python
>>> symbols[0]    # Primer carácter
'A'
>>> symbols[1]    # Segundo carácter
'A'
>>> symbols[2]    # Tercer carácter
'P'
>>> symbols[-1]   # Último carácter
'O'
>>> symbols[-2]   # Penúltimo carácter
'C'
```

También podemos extraer subcadenas utilizando el corte (slicing). El corte nos permite obtener una parte de la cadena especificando un índice de inicio y un índice de fin. La sintaxis para el corte es `string[start:end]`, donde la subcadena incluye caracteres desde el índice de inicio hasta (pero sin incluir) el índice de fin.

```python
>>> symbols[:4]    # Primeros 4 caracteres
'AAPL'
>>> symbols[-3:]   # Últimos 3 caracteres
'SCO'
>>> symbols[5:8]   # Caracteres desde el índice 5 hasta el 7
'IBM'
```

## Inmutabilidad de las cadenas

Las cadenas en Python son inmutables, lo que significa que una vez que se crea una cadena, no se pueden cambiar sus caracteres individuales. Si intentas modificar un carácter en una cadena, Python generará un error.

Intentemos cambiar el primer carácter de nuestra cadena `symbols`:

```python
>>> symbols[0] = 'a'    # Esto causará un error
```

Deberías ver un error como este:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

Este error indica que no podemos asignar un nuevo valor a un carácter individual en una cadena porque las cadenas son inmutables.

## Concatenación de cadenas

Aunque no podemos modificar las cadenas directamente, podemos crear nuevas cadenas a través de la concatenación. La concatenación significa unir dos o más cadenas. En Python, podemos usar el operador `+` para concatenar cadenas.

```python
>>> symbols += ' GOOG'    # Agregar un nuevo símbolo
>>> symbols
'AAPL IBM MSFT YHOO SCO GOOG'

>>> symbols = 'HPQ ' + symbols    # Agregar un nuevo símbolo al principio
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

Es importante recordar que estas operaciones crean nuevas cadenas en lugar de modificar la cadena original. La cadena original permanece sin cambios, y se crea una nueva cadena con el valor combinado.

## Comprobación de subcadenas

Para comprobar si una subcadena existe dentro de una cadena, podemos usar el operador `in`. El operador `in` devuelve `True` si se encuentra la subcadena en la cadena y `False` en caso contrario.

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
```

Observa que 'AA' devuelve `True` porque se encuentra dentro de "AAPL". Esta es una forma útil de buscar texto específico dentro de una cadena más grande.

## Métodos de cadenas

Las cadenas en Python vienen con numerosos métodos incorporados que nos permiten realizar diversas operaciones en cadenas. Estos métodos son funciones asociadas con el objeto de cadena y se pueden llamar utilizando la notación de punto (`string.method()`).

```python
>>> symbols.lower()    # Convertir a minúsculas
'hpq aapl ibm msft yhoo sco goog'

>>> symbols    # La cadena original permanece sin cambios
'HPQ AAPL IBM MSFT YHOO SCO GOOG'

>>> lowersyms = symbols.lower()    # Guardar el resultado en una nueva variable
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'

>>> symbols.find('MSFT')    # Encontrar el índice de inicio de una subcadena
13
>>> symbols[13:17]    # Verificar la subcadena en esa posición
'MSFT'

>>> symbols = symbols.replace('SCO','')    # Reemplazar una subcadena
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
```

Cuando hayas terminado de experimentar, puedes salir de la shell de Python utilizando el siguiente comando:

```python
>>> exit()
```
