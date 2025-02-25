# Kommentar

Wenn Sie beginnen, mit dem Interpreter zu experimentieren, möchten Sie oft mehr über die von verschiedenen Objekten unterstützten Operationen wissen. Beispielsweise wie können Sie herausfinden, welche Operationen auf einem String verfügbar sind?

Je nach Ihrem Python-Umgebung können Sie möglicherweise eine Liste der verfügbaren Methoden über die Tab-Vervollständigung sehen. Beispielsweise versuchen Sie, dies einzugeben:

```python
>>> s = 'hello world'
>>> s.<tab taste>
>>>
```

Wenn das Drücken der Tab-Taste nichts bewirkt, können Sie auf die integrierte `dir()`-Funktion zurückgreifen. Beispielsweise:

```python
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__',..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip','split','splitlines','startswith','strip','swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
```

`dir()` liefert eine Liste aller Operationen, die nach dem `(.)` erscheinen können. Verwenden Sie die `help()`-Anweisung, um weitere Informationen über eine bestimmte Operation zu erhalten:

```python
>>> help(s.upper)
Hilfe zu eingebauter Funktion upper:

upper(...)
    S.upper() -> string

    Gibt eine Kopie der Zeichenkette S in Großbuchstaben zurück.
>>>
```
