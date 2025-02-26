# Mehrere Dekoratoren und Methoden

Es kann etwas kompliziert werden, wenn Dekoratoren auf Methoden in einer Klasse angewendet werden. Versuche, deinen `@logged`-Dekorator auf die Methoden in der folgenden Klasse anzuwenden.

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

Funktioniert es überhaupt? (Hinweis: nein). Gibt es eine Möglichkeit, den Code zu reparieren, sodass es funktioniert? Beispielsweise, kannst du es so gestalten, dass das folgende Beispiel funktioniert?

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
