# Importations relatives

Au lieu d'utiliser directement le nom du package, vous pouvez utiliser `.` pour vous référer au package actuel.

```python
from. import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Syntaxe :

```python
from. import modname
```

Cela facilite la renommation du package.
