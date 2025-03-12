# Comprendiendo las clases de Python

En Python, una clase actúa como un modelo (blueprint) para crear objetos. La programación orientada a objetos es un enfoque poderoso que nos permite organizar nuestro código de manera efectiva. Lo hace agrupando datos y funciones relacionados. De esta manera, podemos manejar programas complejos con mayor facilidad y hacer que nuestro código sea más modular y mantenible.

Una clase de Python se compone de dos componentes principales:

- **Atributos**: Son variables que almacenan datos dentro de una clase. Puedes pensar en los atributos como las características o propiedades de un objeto. Por ejemplo, si estamos creando una clase para representar a una persona, los atributos podrían ser el nombre, la edad y la altura de la persona.
- **Métodos**: Son funciones que pertenecen a una clase y pueden acceder o modificar sus atributos. Los métodos definen las acciones que un objeto puede realizar. Usando el ejemplo de la clase persona, un método podría ser una función que calcula la edad de la persona en meses.

Las clases son extremadamente útiles ya que proporcionan una forma de crear código reutilizable y modelar conceptos del mundo real. En este laboratorio, crearemos una clase `Stock`. Esta clase se utilizará para representar información de acciones (stocks), como el nombre de la acción, el número de acciones y el precio por acción.

A continuación, se muestra la estructura básica de una clase de Python:

```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    def method_name(self):
        # Code that uses the attributes
        return result
```

El método `__init__` es un método especial en las clases de Python. Se llama automáticamente cuando creamos un nuevo objeto a partir de la clase. Este método se utiliza para inicializar los atributos del objeto. El parámetro `self` es una referencia a la instancia de la clase. Se utiliza para acceder a los atributos y métodos desde dentro de la clase. Cuando llamamos a un método en un objeto, Python pasa automáticamente el propio objeto como el primer argumento, por lo que usamos `self` en las definiciones de los métodos. Esto nos permite trabajar con los atributos de la instancia específica y realizar operaciones en ellos.
