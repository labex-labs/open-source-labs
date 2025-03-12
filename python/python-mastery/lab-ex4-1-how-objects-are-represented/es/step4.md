# Entendiendo la relación entre clases e instancias

Ahora, vamos a explorar cómo están relacionadas las clases y las instancias en Python, y cómo funciona la búsqueda de métodos. Este es un concepto importante porque te ayuda a entender cómo Python encuentra y utiliza métodos y atributos cuando trabajas con objetos.

Primero, veamos a qué clase pertenecen nuestras instancias. Saber la clase de una instancia es crucial, ya que nos dice dónde Python buscará los métodos y atributos relacionados con esa instancia.

```python
>>> goog.__class__
<class '__main__.SimpleStock'>
>>> ibm.__class__
<class '__main__.SimpleStock'>
```

Ambas instancias tienen una referencia a la clase `SimpleStock`. Esta referencia es como un puntero que Python utiliza cuando necesita buscar métodos. Cuando llamas a un método en una instancia, Python utiliza esta referencia para encontrar la definición adecuada del método.

Cuando llamas a un método en una instancia, Python sigue estos pasos:

1. Busca el atributo en el `__dict__` de la instancia. El `__dict__` de una instancia es como un área de almacenamiento donde se guardan todos los atributos específicos de la instancia.
2. Si no lo encuentra, verifica el `__dict__` de la clase. El `__dict__` de la clase almacena todos los atributos y métodos que son comunes a todas las instancias de esa clase.
3. Si lo encuentra en la clase, devuelve ese atributo.

Veamos esto en acción. Primero, verificamos que el método `cost` no está en los diccionarios de las instancias. Este paso nos ayuda a entender que el método `cost` no es específico de cada instancia, sino que está definido a nivel de clase.

```python
>>> 'cost' in goog.__dict__
False
>>> 'cost' in ibm.__dict__
False
```

Entonces, ¿de dónde viene el método `cost`? Veamos la clase. Al mirar el `__dict__` de la clase, podemos averiguar dónde está definido el método `cost`.

```python
>>> SimpleStock.__dict__['cost']
<function SimpleStock.cost at 0x7f...>
```

El método está definido en la clase, no en las instancias. Cuando llamas a `goog.cost()`, Python no encuentra `cost` en `goog.__dict__`, así que busca en `SimpleStock.__dict__` y lo encuentra allí.

En realidad, puedes llamar al método directamente desde el diccionario de la clase, pasando la instancia como primer argumento (que se convierte en `self`). Esto muestra cómo Python llama internamente a los métodos cuando usas la sintaxis normal instancia.método().

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.0
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
```

Esto es esencialmente lo que Python hace detrás de escena cuando llamas a `goog.cost()`.

Ahora, agreguemos un atributo de clase. Los atributos de clase son compartidos por todas las instancias. Esto significa que todas las instancias de la clase pueden acceder a este atributo, y se almacena solo una vez a nivel de clase.

```python
>>> SimpleStock.exchange = 'NASDAQ'
>>> goog.exchange
'NASDAQ'
>>> ibm.exchange
'NASDAQ'
```

Ambas instancias pueden acceder al atributo `exchange`, pero no está almacenado en sus diccionarios individuales. Verifiquemos esto comprobando los diccionarios de la instancia y de la clase.

```python
>>> 'exchange' in goog.__dict__
False
>>> 'exchange' in SimpleStock.__dict__
True
>>> SimpleStock.__dict__['exchange']
'NASDAQ'
```

Esto demuestra que:

1. Los atributos de clase son compartidos por todas las instancias. Todas las instancias pueden acceder al mismo atributo de clase sin tener su propia copia.
2. Python verifica primero el diccionario de la instancia, luego el diccionario de la clase. Este es el orden en el que Python busca atributos cuando intentas acceder a ellos en una instancia.
3. Las clases actúan como un repositorio de datos y comportamientos (métodos) compartidos. La clase almacena todos los atributos y métodos comunes que pueden ser utilizados por todas sus instancias.

Si modificamos un atributo de instancia con el mismo nombre, se oculta el atributo de clase. Esto significa que cuando accedes al atributo en esa instancia, Python utilizará el valor específico de la instancia en lugar del valor a nivel de clase.

```python
>>> ibm.exchange = 'NYSE'
>>> ibm.exchange
'NYSE'
>>> goog.exchange  # Todavía usando el atributo de clase
'NASDAQ'
>>> ibm.__dict__['exchange']
'NYSE'
```

Ahora `ibm` tiene su propio atributo `exchange` que oculta el atributo de clase, mientras que `goog` sigue usando el atributo de clase.
