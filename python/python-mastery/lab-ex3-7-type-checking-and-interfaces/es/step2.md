# Clases Base Abstractas

Modifica la clase base `TableFormatter` para que se defina como una clase base abstracta adecuada utilizando el módulo `abc`. Una vez que hayas hecho eso, intenta este experimento:

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

Aquí, la clase base abstracta capturó un error de ortografía en la clase, el hecho de que el método `headings()` se haya dado incorrectamente como `headers()`.
