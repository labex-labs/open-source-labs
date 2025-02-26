# Usando Herencia

La herencia a veces se utiliza para organizar objetos relacionados.

```python
class Shape:
 ...

class Circle(Shape):
 ...

class Rectangle(Shape):
 ...
```

Piensa en una jerarquía lógica o taxonomía. Sin embargo, un uso más común (y práctico) está relacionado con hacer código reutilizable o extensible. Por ejemplo, un framework podría definir una clase base y te instruiría para personalizarla.

```python
class CustomHandler(TCPHandler):
    def handle_request(self):
     ...
        # Procesamiento personalizado
```

La clase base contiene un código de uso general. Tu clase hereda y personaliza partes específicas.
