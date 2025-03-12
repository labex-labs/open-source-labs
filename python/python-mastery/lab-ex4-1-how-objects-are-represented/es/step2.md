# Explorando el diccionario interno de los objetos

En Python, los objetos son un concepto fundamental. Un objeto se puede considerar como un contenedor que almacena datos y tiene ciertos comportamientos. Uno de los aspectos interesantes de los objetos de Python es cómo almacenan sus atributos. Los atributos son como variables que pertenecen a un objeto. Python almacena estos atributos en un diccionario especial, que se puede acceder a través del atributo `__dict__`. Este diccionario es una parte interna del objeto y es donde Python lleva el registro de todos los datos asociados con ese objeto.

Echemos un vistazo más de cerca a esta estructura interna utilizando nuestras instancias de `SimpleStock`. En Python, una instancia es un objeto individual creado a partir de una clase. Por ejemplo, si `SimpleStock` es una clase, `goog` e `ibm` son instancias de esa clase.

Para ver el diccionario interno de estas instancias, podemos usar la shell interactiva de Python. La shell interactiva de Python es una excelente herramienta para probar rápidamente el código y ver los resultados. En la shell interactiva de Python, escribe los siguientes comandos para inspeccionar el atributo `__dict__` de nuestras instancias:

```python
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1}
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
```

Cuando ejecutas estos comandos, la salida muestra que cada instancia tiene su propio diccionario interno. Este diccionario contiene todos los atributos de la instancia. Por ejemplo, en la instancia `goog`, los atributos `name`, `shares` y `price` se almacenan en el diccionario con sus valores correspondientes. Así es como Python implementa los atributos de los objetos detrás de escena. Cada objeto tiene un diccionario privado que contiene todos sus atributos.

Es importante entender lo que el atributo `__dict__` revela sobre la implementación interna de nuestros objetos:

1. Las claves en el diccionario corresponden a los nombres de los atributos. Por ejemplo, en la instancia `goog`, la clave `'name'` corresponde al atributo `name` del objeto.
2. Los valores en el diccionario son los valores de los atributos. Entonces, el valor `'GOOG'` es el valor del atributo `name` para la instancia `goog`.
3. Cada instancia tiene su propio `__dict__` separado. Esto significa que los atributos de una instancia son independientes de los atributos de otra instancia. Por ejemplo, el atributo `shares` de la instancia `goog` puede ser diferente del atributo `shares` de la instancia `ibm`.

Este enfoque basado en diccionarios permite que Python sea muy flexible con los objetos. Como veremos en el siguiente paso, podemos aprovechar esta flexibilidad para modificar y acceder a los atributos de los objetos de varias maneras.
