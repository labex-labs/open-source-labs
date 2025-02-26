# Classes de base abstraites

Modifiez la classe de base `TableFormatter` de sorte qu'elle soit définie comme une vraie classe de base abstraite à l'aide du module `abc`. Une fois que vous avez fait cela, essayez cet exemple :

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

Ici, la classe de base abstraite a détecté une erreur de frappe dans la classe - le fait que la méthode `headings()` ait été incorrectement écrite `headers()`.
