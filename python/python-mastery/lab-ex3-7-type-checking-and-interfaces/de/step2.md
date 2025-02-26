# Abstrakte Basisklassen

Ändern Sie die Basisklasse `TableFormatter` so, dass sie als richtige abstrakte Basisklasse mithilfe des `abc`-Moduls definiert wird. Nachdem Sie das getan haben, versuchen Sie dieses Experiment:

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

Hier hat die abstrakte Basisklasse einen Tippfehler in der Klasse erkannt – die Tatsache, dass die `headings()`-Methode falsch als `headers()` angegeben wurde.
