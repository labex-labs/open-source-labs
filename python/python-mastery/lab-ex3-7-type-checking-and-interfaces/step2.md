# Abstract Base Classes

Modify the `TableFormatter` base class so that it is defined as a proper abstract base class using the `abc` module. Once you have done that, try this experiment:

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

Here, the abstract base class caught a spelling error in the class--the fact that the `headings()` method was incorrectly given as `headers()`.
