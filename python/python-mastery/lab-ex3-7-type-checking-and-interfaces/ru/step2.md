# Абстрактные базовые классы

Измените базовый класс `TableFormatter`, чтобы он был определен как правильный абстрактный базовый класс с использованием модуля `abc`. После этого попробуйте этот эксперимент:

```python
>>> class NewFormatter(TableFormatter):
        def headers(self, headings):
            pass
        def row(self, rowdata):
            pass

>>> f = NewFormatter()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class NewFormatter with abstract methods headings
>>>
```

Здесь абстрактный базовый класс поймал орфографическую ошибку в классе - то, что метод `headings()` был неправильно записан как `headers()`.
