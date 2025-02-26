# Dicts et Modules

Dans un module, un dictionnaire contient toutes les variables et fonctions globales.

```python
# foo.py

x = 42
def bar():
  ...

def spam():
  ...
```

Si vous examinez `foo.__dict__` ou `globals()`, vous verrez le dictionnaire.

```python
{
    'x' : 42,
    'bar' : <function bar>,
   'spam' : <function spam>
}
```
