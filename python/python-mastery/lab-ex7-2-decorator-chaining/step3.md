# Multiple decorators and methods

Things can get a bit dicey when decorators are applied to methods in a class. Try applying your `@logged` decorator to the methods in the following class.

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

Does it even work at all? (hint: no). Is there any way to fix the code so that it works? For example, can you make it so the following example works?

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
