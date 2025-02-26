# Несколько декораторов и методы

Ситуация может стать несколько запутанной, когда декораторы применяются к методам класса. Попробуйте применить декоратор `@logged` к методам следующего класса.

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

Работает ли это вообще? (подсказка: нет). Есть ли какой-то способ исправить код, чтобы он работал? Например, можно ли сделать так, чтобы следующий пример работал?

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
