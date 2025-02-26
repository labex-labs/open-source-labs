# Dekoratoren

Das Umhüllen von Funktionen mit Wrappern ist in Python extrem üblich. So üblich, dass es eine spezielle Syntax dafür gibt.

```python
def add(x, y):
    return x + y
add = logged(add)

# Spezielle Syntax
@logged
def add(x, y):
    return x + y
```

Die spezielle Syntax führt genau die gleichen Schritte wie oben gezeigt aus. Ein Dekorator ist einfach nur neue Syntax. Man sagt, dass er die Funktion _dekoriert_.
