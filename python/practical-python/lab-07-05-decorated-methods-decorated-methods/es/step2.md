# Métodos estáticos

`@staticmethod` se utiliza para definir los llamados _métodos estáticos_ de una clase (del C++/Java). Un método estático es una función que es parte de la clase, pero que _no_ opera sobre instancias.

```python
class Foo(object):
    @staticmethod
    def bar(x):
        print('x =', x)

>>> Foo.bar(2) # x=2
>>>
```

Los métodos estáticos a veces se utilizan para implementar el código de soporte interno para una clase. Por ejemplo, código para ayudar a administrar las instancias creadas (gestión de memoria, recursos del sistema, persistencia, bloqueo, etc.). También se utilizan en ciertos patrones de diseño (no se discuten aquí).
