# Ejercicio 5.3: El papel de las clases

Las definiciones que componen una definición de clase son compartidas por todas las instancias de esa clase. Observe que todas las instancias tienen un enlace de vuelta a su clase asociada:

```python
>>> goog.__class__
... mira la salida...
>>> ibm.__class__
... mira la salida...
>>>
```

Intenta llamar a un método en las instancias:

```python
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
>>>
```

Observe que el nombre 'cost' no está definido en `goog.__dict__` ni en `ibm.__dict__`. En su lugar, está siendo suministrado por el diccionario de la clase. Prueba esto:

```python
>>> Stock.__dict__['cost']
... mira la salida...
>>>
```

Intenta llamar al método `cost()` directamente a través del diccionario:

```python
>>> Stock.__dict__['cost'](goog)
49010.0
>>> Stock.__dict__['cost'](ibm)
4561.5
>>>
```

Observe cómo se está llamando a la función definida en la definición de la clase y cómo el argumento `self` obtiene la instancia.

Intenta agregar un nuevo atributo a la clase `Stock`:

```python
>>> Stock.foo = 42
>>>
```

Observe cómo este nuevo atributo ahora aparece en todas las instancias:

```python
>>> goog.foo
42
>>> ibm.foo
42
>>>
```

Sin embargo, observe que no es parte del diccionario de la instancia:

```python
>>> goog.__dict__
... mira la salida y observa que no hay un atributo 'foo'...
>>>
```

La razón por la cual se puede acceder al atributo `foo` en las instancias es que Python siempre verifica el diccionario de la clase si no puede encontrar algo en la instancia misma.

Nota: Esta parte del ejercicio ilustra algo conocido como una variable de clase. Suponga, por ejemplo, que tiene una clase como esta:

```python
class Foo(object):
     a = 13                  # Variable de clase
     def __init__(self,b):
         self.b = b          # Variable de instancia
```

En esta clase, la variable `a`, asignada en el cuerpo de la clase misma, es una "variable de clase". Es compartida por todas las instancias que se crean. Por ejemplo:

```python
>>> f = Foo(10)
>>> g = Foo(20)
>>> f.a          # Inspecciona la variable de clase (es la misma para ambas instancias)
13
>>> g.a
13
>>> f.b          # Inspecciona la variable de instancia (es diferente)
10
>>> g.b
20
>>> Foo.a = 42   # Cambia el valor de la variable de clase
>>> f.a
42
>>> g.a
42
>>>
```
