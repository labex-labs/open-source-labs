# Definiciones globales

Todo lo definido en el ámbito _global_ es lo que llena el espacio de nombres del módulo. Considere dos módulos que definen la misma variable `x`.

```python
# foo.py
x = 42
def grok(a):
 ...
```

```python
# bar.py
x = 37
def spam(a):
 ...
```

En este caso, las definiciones de `x` se refieren a variables diferentes. Una es `foo.x` y la otra es `bar.x`. Diferentes módulos pueden usar los mismos nombres y esos nombres no se confundirán entre sí.

**Los módulos están aislados.**
