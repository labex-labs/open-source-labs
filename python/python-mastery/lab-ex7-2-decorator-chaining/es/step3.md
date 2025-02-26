# Varios decoradores y métodos

Las cosas pueden ponerse un poco complicadas cuando se aplican decoradores a métodos en una clase. Intenta aplicar tu decorador `@logged` a los métodos de la siguiente clase.

```python
class Spam:
    @logged
    def instance_method(self):
        pass

    @logged
    @classmethod
    def class_method(cls):
        pass

    @logged
    @staticmethod
    def static_method():
        pass

    @logged
    @property
    def property_method(self):
        pass
```

¿Funciona en absoluto? (pista: no). ¿Hay alguna manera de corregir el código para que funcione? Por ejemplo, ¿puedes hacer que el siguiente ejemplo funcione?

```python
>>> s = Spam()
>>> s.instance_method()
instance_method
>>> Spam.class_method()
class_method
>>> Spam.static_method()
static_method
>>> s.property_method
property_method
>>>
```
