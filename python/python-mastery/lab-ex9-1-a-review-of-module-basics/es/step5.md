# recarga() dañada

Crea una instancia:

```python
>>> import simplemod
>>> s = simplemod.Spam()
>>> s.yow()
¡Guau!
>>>
```

Ahora, vaya al archivo `simplemod.py` y cambie la implementación de `Spam.yow()` a la siguiente:

```python
# simplemod.py
...

class Spam:
    def yow(self):
        print('Más ¡Guau!')
```

Ahora, observe lo que sucede en una recarga. No reinicie Python para esta parte.

```python
>>> importlib.reload(simplemod)
Cargado simplemod
<module'simplemod' from'simplemod.py'>
>>> s.yow()
'¡Guau!'
>>> t = simplemod.Spam()
>>> t.yow()
'Más ¡Guau!'
>>>
```

Observe cómo tiene dos instancias de `Spam`, pero están usando diferentes implementaciones del método `yow()`. Sí, en realidad ambas versiones del código se cargan al mismo tiempo. También encontrará otras rarezas. Por ejemplo:

```python
>>> s
<simplemod.Spam objeto en 0x1006940b8>
>>> isinstance(s, simplemod.Spam)
Falso
>>> isinstance(t, simplemod.Spam)
Verdadero
>>>
```

En resumen: Probablemente sea mejor no confiar en la recarga para nada importante. Podría estar bien si solo está intentando depurar algunas cosas (siempre y cuando esté al tanto de sus limitaciones y peligros).
