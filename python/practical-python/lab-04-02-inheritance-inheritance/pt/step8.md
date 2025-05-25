# Usando Herança (Inheritance)

A herança é, por vezes, usada para organizar objetos relacionados.

```python
class Shape:
    ...

class Circle(Shape):
    ...

class Rectangle(Shape):
    ...
```

Pense em uma hierarquia lógica ou taxonomia. No entanto, um uso mais comum (e prático) está relacionado à criação de código reutilizável ou extensível. Por exemplo, um framework pode definir uma classe base e instruí-lo a personalizá-la.

```python
class CustomHandler(TCPHandler):
    def handle_request(self):
        ...
        # Custom processing
```

A classe base contém algum código de uso geral. Sua classe herda e personaliza partes específicas.
