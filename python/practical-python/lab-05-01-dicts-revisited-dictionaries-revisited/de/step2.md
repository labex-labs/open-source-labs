# Dicts and Modules

Innerhalb eines Moduls enthält ein Wörterbuch alle globalen Variablen und Funktionen.

```python
# foo.py

x = 42
def bar():
  ...

def spam():
  ...
```

Wenn Sie `foo.__dict__` oder `globals()` untersuchen, werden Sie das Wörterbuch sehen.

```python
{
    'x' : 42,
    'bar' : <function bar>,
   'spam' : <function spam>
}
```
