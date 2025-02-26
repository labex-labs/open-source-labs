# Delegación como alternativa a la herencia

La delegación a veces se utiliza como alternativa a la herencia. La idea es casi la misma que la clase proxy que definiste en la parte (b). Intenta definir la siguiente clase:

```python
>>> class Spam:
        def a(self):
            print('Spam.a')
        def b(self):
            print('Spam.b')

>>>
```

Ahora, crea una clase que se encierre en ella y redefina algunos de los métodos:

```python
>>> class MySpam:
        def __init__(self):
            self._spam = Spam()
        def a(self):
            print('MySpam.a')
            self._spam.a()
        def c(self):
            print('MySpam.c')
        def __getattr__(self, name):
            return getattr(self._spam, name)

>>> s = MySpam()
>>> s.a()
MySpam.a
Spam.a
>>> s.b()
Spam.b
>>> s.c()
MySpam.c
>>>
```

Observa detenidamente que la clase resultante se parece mucho a la herencia. Por ejemplo, el método `a()` está haciendo algo similar a la llamada a `super()`. El método `b()` se obtiene a través del método `__getattr__()` que delega en la instancia interna de `Spam`.

**Discusión**

El método `__getattr__()` se define comúnmente en las clases que actúan como envoltorios de otros objetos. Sin embargo, debes ser consciente de que el proceso de envolver otro objeto de esta manera a menudo introduce otras complejidades. Por ejemplo, el objeto envoltorio podría romper la comprobación de tipos si cualquier otra parte de la aplicación está utilizando la función `isinstance()`.

La delegación de métodos a través de `__getattr__()` también no funciona con métodos especiales como `__getitem__()`, `__enter__()` y demás. Si una clase utiliza ampliamente tales métodos, tendrás que proporcionar funciones similares en tu clase envolvente.
